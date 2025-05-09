package com.myproject;

import java.util.HashMap;
import java.util.Map;

public class StockRealtimePriceView implements StockViewer {
    private final Map<String, Double> lastPrices = new HashMap<>();

    @Override
    public void onUpdate(StockPrice stockPrice) {
        // TODO: Implement logic to check if price has changed and log it
        String stockCode = stockPrice.getCode();
        double currentPrice = stockPrice.getAvgPrice();
        double lastPrice = lastPrices.getOrDefault(stockCode, 0.0);
        lastPrices.put(stockCode, currentPrice);
        if (currentPrice != lastPrice) {
            Logger.logRealtime(stockCode, currentPrice);
        }
    }
}
