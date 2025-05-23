package com.myproject;

import java.util.HashMap;
import java.util.Map;

public class StockAlertView implements StockViewer {
    private double alertThresholdHigh;
    private double alertThresholdLow;
    private Map<String, Double> lastAlertedPrices = new HashMap<>(); // TODO: Stores last alerted price per stock

    public StockAlertView(double highThreshold, double lowThreshold) {
        // TODO: Implement constructor
        this.alertThresholdHigh = highThreshold;
        this.alertThresholdLow = lowThreshold;
    }

    @Override
    public void onUpdate(StockPrice stockPrice) {
        // TODO: Implement alert logic based on threshold conditions
        String stockCode = stockPrice.getCode();
        double currentPrice = stockPrice.getAvgPrice();
        double lastPrice = lastAlertedPrices.getOrDefault(stockCode, 0.0);
        lastAlertedPrices.put(stockCode, currentPrice);
        // if (currentPrice > alertThresholdHigh) {
        //     alertAbove(stockCode, currentPrice);
        // } else if (currentPrice < alertThresholdLow) {
        //     alertBelow(stockCode, currentPrice);
        // }
        if (currentPrice > alertThresholdHigh && (lastPrice <= alertThresholdHigh)) {
            alertAbove(stockCode, currentPrice);
        } else if (currentPrice < alertThresholdLow && (lastPrice >= alertThresholdLow)) {
            alertBelow(stockCode, currentPrice);
        }
    }

    private void alertAbove(String stockCode, double price) {
        // TODO: Call Logger to log the alert
        Logger.logAlert(stockCode, price);
    }

    private void alertBelow(String stockCode, double price) {
        // TODO: Call Logger to log the alert
        Logger.logAlert(stockCode, price);
    }
}
