SET search_path TO amazon, public;
CREATE TABLE IF NOT EXISTS "buyer" (
  "unnamed__0" INTEGER,
  "buyer_id" VARCHAR,
  PRIMARY KEY ("buyer_id")
);

CREATE TABLE IF NOT EXISTS "carrier" (
  "unnamed__0" VARCHAR,
  "carrier_id" VARCHAR,
  "carrier_name" VARCHAR,
  PRIMARY KEY ("carrier_id")
);

CREATE TABLE IF NOT EXISTS "cart_items" (
  "unnamed__0" VARCHAR,
  "cart_id" VARCHAR,
  "p_id" VARCHAR,
  "qty" VARCHAR
);

CREATE TABLE IF NOT EXISTS "cart" (
  "unnamed__0" VARCHAR,
  "cart_id" VARCHAR,
  "buyer_id" VARCHAR,
  "total_qty" VARCHAR,
  "total_price" VARCHAR,
  PRIMARY KEY ("cart_id")
);

CREATE TABLE IF NOT EXISTS "category" (
  "unnamed__0" INTEGER,
  "category_id" INTEGER,
  "name" VARCHAR,
  "c_desc" VARCHAR,
  PRIMARY KEY ("category_id")
);

CREATE TABLE IF NOT EXISTS "customer_payment" (
  "unnamed__0" INTEGER,
  "payment_id" INTEGER,
  "c_id" VARCHAR,
  "is_default" INTEGER
);

CREATE TABLE IF NOT EXISTS "customer_shipping" (
  "unnamed__0" INTEGER,
  "address_id" INTEGER,
  "c_id" VARCHAR,
  "is_default" INTEGER
);

CREATE TABLE IF NOT EXISTS "customer" (
  "unnamed__0" INTEGER,
  "c_id" VARCHAR,
  "fname" VARCHAR,
  "lname" VARCHAR,
  "phone" INTEGER,
  "email" VARCHAR,
  "pwd" VARCHAR,
  PRIMARY KEY ("c_id")
);

CREATE TABLE IF NOT EXISTS "daily_deals" (
  "unnamed__0" VARCHAR,
  "p_id" VARCHAR,
  "deal_date" VARCHAR,
  "discount" VARCHAR,
  PRIMARY KEY ("p_id")
);

CREATE TABLE IF NOT EXISTS "discount" (
  "unnamed__0" VARCHAR,
  "discount_id" VARCHAR,
  "discount_name" VARCHAR,
  "d_desc" VARCHAR,
  "discount_amt" VARCHAR,
  PRIMARY KEY ("discount_id")
);

CREATE TABLE IF NOT EXISTS "orders" (
  "unnamed__0" INTEGER,
  "order_id" INTEGER,
  "buyer_id" VARCHAR,
  "discount_id" NUMERIC,
  "payment_id" INTEGER,
  "order_date" TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "payment_details" (
  "unnamed__0" INTEGER,
  "payment_id" INTEGER,
  "card_no" BIGINT,
  "cvv" INTEGER,
  "expiry_date" TIMESTAMP,
  "billing_address" VARCHAR,
  PRIMARY KEY ("payment_id")
);

CREATE TABLE IF NOT EXISTS "product_images" (
  "unnamed__0" INTEGER,
  "p_id" VARCHAR,
  "p_image" VARCHAR,
  PRIMARY KEY ("p_id")
);

CREATE TABLE IF NOT EXISTS "product_reviews" (
  "unnamed__0" INTEGER,
  "p_id" VARCHAR,
  "review_id" INTEGER
);

CREATE TABLE IF NOT EXISTS "product" (
  "unnamed__0" INTEGER,
  "p_id" VARCHAR,
  "p_name" VARCHAR,
  "p_desc" TEXT,
  "price" NUMERIC,
  "qty" INTEGER,
  "category_id" INTEGER
);

CREATE TABLE IF NOT EXISTS "returns" (
  "unnamed__0" VARCHAR,
  "return_id" VARCHAR,
  "buyer_id" VARCHAR,
  "p_id" VARCHAR,
  "order_id" VARCHAR
);

CREATE TABLE IF NOT EXISTS "review_images" (
  "unnamed__0" INTEGER,
  "review_id" INTEGER,
  "review_img" VARCHAR,
  PRIMARY KEY ("review_id")
);

CREATE TABLE IF NOT EXISTS "review" (
  "unnamed__0" INTEGER,
  "review_id" INTEGER,
  "buyer_id" VARCHAR,
  "r_desc" TEXT,
  "title" VARCHAR,
  "rating" INTEGER,
  "seller_product_flag" VARCHAR,
  PRIMARY KEY ("review_id")
);

CREATE TABLE IF NOT EXISTS "seller_products" (
  "unnamed__0" INTEGER,
  "seller_id" VARCHAR,
  "p_id" VARCHAR
);

CREATE TABLE IF NOT EXISTS "seller_reviews" (
  "unnamed__0" INTEGER,
  "seller_id" VARCHAR,
  "review_id" INTEGER
);

CREATE TABLE IF NOT EXISTS "seller" (
  "unnamed__0" INTEGER,
  "seller_id" VARCHAR,
  "seller_type" VARCHAR,
  PRIMARY KEY ("seller_id")
);

CREATE TABLE IF NOT EXISTS "shipment" (
  "unnamed__0" VARCHAR,
  "shipping_id" VARCHAR,
  "order_id" VARCHAR,
  "p_id" VARCHAR,
  "carrier_id" VARCHAR,
  "shipment_type" VARCHAR,
  "status" VARCHAR,
  "est_delivery_date" VARCHAR,
  "actual_delivery_date" VARCHAR
);

CREATE TABLE IF NOT EXISTS "shipping_details" (
  "unnamed__0" INTEGER,
  "address_id" INTEGER,
  "street_address" VARCHAR,
  "city" VARCHAR,
  "state" VARCHAR,
  "zip" INTEGER,
  "country" VARCHAR,
  "phone" INTEGER,
  PRIMARY KEY ("address_id")
);

CREATE TABLE IF NOT EXISTS "subscription" (
  "unnamed__0" INTEGER,
  "subscription_id" INTEGER,
  "c_id" VARCHAR,
  "start_date" TIMESTAMP,
  "end_date" TIMESTAMP,
  PRIMARY KEY ("subscription_id")
);

CREATE TABLE IF NOT EXISTS "wishlist_item" (
  "unnamed__0" INTEGER,
  "product_id" VARCHAR,
  "buyer_id" VARCHAR
);

ALTER TABLE "cart_items" ADD CONSTRAINT fk_cart_items_cart_id FOREIGN KEY ("cart_id") REFERENCES "cart" ("cart_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "cart" ADD CONSTRAINT fk_cart_buyer_id FOREIGN KEY ("buyer_id") REFERENCES "buyer" ("buyer_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "orders" ADD CONSTRAINT fk_orders_buyer_id FOREIGN KEY ("buyer_id") REFERENCES "buyer" ("buyer_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "orders" ADD CONSTRAINT fk_orders_discount_id FOREIGN KEY ("discount_id") REFERENCES "discount" ("discount_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "product_reviews" ADD CONSTRAINT fk_product_reviews_review_id FOREIGN KEY ("review_id") REFERENCES "review" ("review_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "product" ADD CONSTRAINT fk_product_category_id FOREIGN KEY ("category_id") REFERENCES "category" ("category_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "returns" ADD CONSTRAINT fk_returns_buyer_id FOREIGN KEY ("buyer_id") REFERENCES "buyer" ("buyer_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "review" ADD CONSTRAINT fk_review_buyer_id FOREIGN KEY ("buyer_id") REFERENCES "buyer" ("buyer_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "seller_products" ADD CONSTRAINT fk_seller_products_seller_id FOREIGN KEY ("seller_id") REFERENCES "seller" ("seller_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "seller_reviews" ADD CONSTRAINT fk_seller_reviews_seller_id FOREIGN KEY ("seller_id") REFERENCES "seller" ("seller_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "seller_reviews" ADD CONSTRAINT fk_seller_reviews_review_id FOREIGN KEY ("review_id") REFERENCES "review" ("review_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "shipment" ADD CONSTRAINT fk_shipment_carrier_id FOREIGN KEY ("carrier_id") REFERENCES "carrier" ("carrier_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "wishlist_item" ADD CONSTRAINT fk_wishlist_item_buyer_id FOREIGN KEY ("buyer_id") REFERENCES "buyer" ("buyer_id") DEFERRABLE INITIALLY DEFERRED;