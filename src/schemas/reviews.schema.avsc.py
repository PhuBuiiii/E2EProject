{
  "type": "record",
  "name": "customer_reviews",
  "namespace": "com.airscholar",
  "doc": "Schema for customer reviews",
  "fields": [
    { "name": "review_id",  "type": "string" },
    { "name": "user_id",  "type": "string" },
    { "name": "business_id", "type": "string" },
    { "name": "stars", "type": "float" },
    { "name": "date", "type": "string" },
    { "name": "text",  "type": "string" },
  ]
}