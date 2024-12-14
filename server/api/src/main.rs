use actix_web::{web, App, HttpServer, Responder, HttpResponse, post, get, put};
use rusqlite::{params, Connection, Result};
use serde::{Serialize, Deserialize};
use std::sync::{Arc, Mutex};

#[derive(Serialize)]
struct Message {
    id: i32,
    content: String,
    timestamp: String,
    flush: i32,
    score: i32,
}

#[derive(Deserialize)]
struct Body {
    content: String,
    score: i32,
}

// SQLiteデータベースを初期化
fn init_db() -> Result<Connection> {
    let conn = Connection::open("messages.db")?;
    conn.execute(
        "CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            flush INTEGER DEFAULT 0,
            score INTEGER DEFAULT 0
        )",
        [],
    )?;
    Ok(conn)
}

// POSTエンドポイント: メッセージを保存
#[post("/submit")]
async fn submit(
    data: web::Data<Arc<Mutex<Connection>>>,
    body: web::Json<Body>,
) -> impl Responder {
    let conn = data.lock().unwrap();
    let now = chrono::Local::now().to_rfc3339();

    match conn.execute(
        "INSERT INTO messages (content, flush, timestamp, score) VALUES (?1, ?2, ?3, ?4)",
        params![body.content, 0, now, body.score],
    ) {
        Ok(_) => HttpResponse::Ok().body("Message saved successfully!"),
        Err(e) => {
            eprintln!("Error inserting message: {}", e);
            HttpResponse::InternalServerError().body("Failed to save message")
        }
    }
}

// GETエンドポイント: メッセージを取得
#[get("/messages")]
async fn get_messages(data: web::Data<Arc<Mutex<Connection>>>) -> impl Responder {
    let conn = data.lock().unwrap();
    let mut stmt = match conn.prepare("SELECT id, content, timestamp, flush, score FROM messages") {
        Ok(stmt) => stmt,
        Err(e) => {
            eprintln!("Error preparing statement: {}", e);
            return HttpResponse::InternalServerError().body("Failed to retrieve messages");
        }
    };

    let messages_iter = stmt.query_map([], |row| {
        Ok(Message {
            id: row.get(0)?,
            content: row.get(1)?,
            timestamp: row.get(2)?,
            flush: row.get(3)?,
            score: row.get(4)?,
        })
    });

    match messages_iter {
        Ok(messages) => {
            let messages: Vec<Message> = messages.filter_map(Result::ok).collect();
            HttpResponse::Ok().json(messages)
        }
        Err(e) => {
            eprintln!("Error querying messages: {}", e);
            HttpResponse::InternalServerError().body("Failed to retrieve messages")
        }
    }
}

// PUTエンドポイント: flushの値を一つあげる
#[put("/increment_flush/{id}")]
async fn increment_flush(
    data: web::Data<Arc<Mutex<Connection>>>,
    id: web::Path<i32>,
) -> impl Responder {
    let conn = data.lock().unwrap();

    match conn.execute(
        "UPDATE messages SET flush = flush + 1 WHERE id = ?1",
        params![*id],
    ) {
        Ok(_) => HttpResponse::Ok().body("Flush value incremented successfully!"),
        Err(e) => {
            eprintln!("Error updating flush value: {}", e);
            HttpResponse::InternalServerError().body("Failed to increment flush value")
        }
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // データベースを初期化
    let conn = init_db().unwrap();
    let conn = Arc::new(Mutex::new(conn)); // Arc<Mutex<T>> で共有可能にラップ

    // Actix-webサーバーを起動
    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(conn.clone())) // Arc をクローン
            .service(submit)
            .service(get_messages)
            .service(increment_flush)
    })
    .bind(("0.0.0.0", 8080))?
    .run()
    .await
}
