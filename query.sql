SELECT
  channel_grouping,
  ARRAY_AGG(STRUCT(CAST(date AS DATE FORMAT 'YYYYMMDD') AS date, country, total) ORDER BY date ASC, country ASC) AS transactions
FROM
(
SELECT
  channelGrouping as channel_grouping, 
  date, 
  geoNetwork_country as country, 
  SUM(totals_transactions) as total
FROM 
  `data-to-insights.ecommerce.rev_transactions` 
GROUP BY 
  channel_grouping, 
  date, 
  country
)
GROUP BY 
  channel_grouping
ORDER BY
  channel_grouping DESC;