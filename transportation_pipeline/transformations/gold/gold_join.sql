create or replace view transportation.gold.data as
(select t.id,
t.business_date,
t.city_id,
c.city_name,
t.passenger_category,
t.distance_kms,
t.sales_amt,
t.passenger_rating,
t.driver_rating,
ca.month,
ca.day_of_month,
ca.day_of_week,
ca.month_name,
ca.month_year,
ca.quarter,
ca.quarter_year,
ca.week_of_year,
ca.is_weekday,
ca.is_weekend,
ca.is_holiday as national_holiday from transportation.silver.trip as t
join transportation.silver.city as c
on t.city_id=c.city_id
join transportation.silver.calendar ca
on t.business_date=ca.date);

