package com.hemoconnect.controller;

import com.hemoconnect.service.FirebaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/api/admin")
public class AdminController {

    @Autowired
    private FirebaseService firebaseService;

    // Phase 16: Seeding demo data
    @PostMapping("/seed")
    public ResponseEntity<Map<String, String>> seedDemoData() {
        try {
            firebaseService.resetAndSeedDemoData();
            return ResponseEntity.ok(Map.of("message", "Database successfully reset and seeded with hackathon demo data."));
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", "Failed to seed data: " + e.getMessage()));
        }
    }

    // CORS proxy endpoint to fetch JSON data from external blood bank API registries
    @org.springframework.web.bind.annotation.GetMapping("/fetch-external")
    public ResponseEntity<?> fetchExternalData(@org.springframework.web.bind.annotation.RequestParam String url) {
        try {
            java.net.http.HttpClient client = java.net.http.HttpClient.newHttpClient();
            java.net.http.HttpRequest request = java.net.http.HttpRequest.newBuilder()
                    .uri(java.net.URI.create(url))
                    .timeout(java.time.Duration.ofSeconds(10))
                    .header("Accept", "application/json")
                    .GET()
                    .build();

            java.net.http.HttpResponse<String> response = client.send(request, java.net.http.HttpResponse.BodyHandlers.ofString());
            
            if (response.statusCode() == 200) {
                return ResponseEntity.ok()
                        .header("Content-Type", "application/json")
                        .body(response.body());
            } else {
                return ResponseEntity.status(response.statusCode())
                        .body(Map.of("error", "External URL returned status " + response.statusCode()));
            }
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", "Failed to fetch external resource: " + e.getMessage()));
        }
    }
}
