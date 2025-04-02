package com.myproject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StockFeeder {
    private List<Stock> stockList = new ArrayList<>();
    private Map<String, List<StockViewer>> viewers = new HashMap<>();
    private static volatile StockFeeder instance = null;

    // TODO: Implement Singleton pattern
    private StockFeeder() {}

    public static StockFeeder getInstance() {
        // TODO: Implement Singleton logic
        if(instance == null){
            synchronized (StockFeeder.class){
                if(instance == null){
                    instance = new StockFeeder();
                }
            }
        }
        return instance;
    }

    public void addStock(Stock stock) {
        // TODO: Implement adding a stock to stockList
        stockList.add(stock);
    }

    public void registerViewer(String code, StockViewer stockViewer) {
        // TODO: Implement registration logic, including checking stock existence
        viewers.computeIfAbsent(code, k -> new ArrayList<>()).add(stockViewer);
    }    

    public void unregisterViewer(String code, StockViewer stockViewer) {
        List<StockViewer> stockViewers = viewers.get(code);
        if (stockViewers != null) {
            if (stockViewers.remove(stockViewer)) {
                // Successfully removed the viewer
                if (stockViewers.isEmpty()) {
                    // If no viewers remain for this stock, remove the entry from the map
                    viewers.remove(code);
                }
            } else {
                // Viewer was not registered for this stock
                System.err.println("Error: Viewer not found for stock code: " + code);
            }
        } else {
            // No viewers registered for this stock code
            System.err.println("Error: No viewers registered for stock code: " + code);
        }
    }

    public void notify(StockPrice stockPrice) {
        // TODO: Implement notifying registered viewers about price updates
        List<StockViewer> stockViewers = viewers.get(stockPrice.getCode());
        if (stockViewers != null) {
            for (StockViewer viewer : stockViewers) {
                viewer.onUpdate(stockPrice);
            }
        }
    }
}
