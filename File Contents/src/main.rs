use axum::{
    extract::{Json, Query},
    routing::get,
    Router,
};
use serde::{Deserialize, Serialize};
use std::{net::SocketAddr, sync::Arc};
use tokio::sync::Mutex;
use uuid::Uuid;

#[derive(Debug, Serialize, Clone)]
struct Item {
    id: String,
    title: String,
    description: String,
    tags: Vec<String>,
}

type Index = Arc<Mutex<Vec<Item>>>;

#[derive(Debug, Deserialize)]
struct SearchQuery {
    q: String,
}

#[tokio::main]
async fn main() {
    let index: Index = Arc::new(Mutex::new(vec![
        Item {
            id: Uuid::new_v4().to_string(),
            title: "Rust Async Guide".to_string(),
            description: "Learn async programming in Rust".to_string(),
            tags: vec!["rust".into(), "async".into(), "guide".into()],
        },
        Item {
            id: Uuid::new_v4().to_string(),
            title: "Axum Microservices".to_string(),
            description: "Build services with Axum framework".to_string(),
            tags: vec!["rust".into(), "axum".into(), "microservices".into()],
        },
    ]));

    let app = Router::new()
        .route("/search", get(search_items))
        .with_state(index.clone());

    let addr = SocketAddr::from(([127, 0, 0, 1], 4702));
    println!("🔎 Discovery Service running at http://{}", addr);

    axum::Server::bind(&addr)
        .serve(app.into_make_service_with_state(index))
        .await
        .unwrap();
}

async fn search_items(
    Query(params): Query<SearchQuery>,
    axum::extract::State(index): axum::extract::State<Index>,
) -> Json<Vec<Item>> {
    let items = index.lock().await;
    let results: Vec<Item> = items
        .iter()
        .filter(|item| {
            item.title.to_lowercase().contains(&params.q.to_lowercase())
                || item.description.to_lowercase().contains(&params.q.to_lowercase())
                || item.tags.iter().any(|t| t.contains(&params.q.to_lowercase()))
        })
        .cloned()
        .collect();

    Json(results)
}
