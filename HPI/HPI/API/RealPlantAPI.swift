//
//  RealPlantAPI.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import Foundation
import AsyncHTTPClient

@Observable
public class RealPlantAPI: PlantAPI {
    private let baseUrl = URL(string: "localhost:8000")!
    private let client = HTTPClient()
    private let decoder = {
        let dec = JSONDecoder()
        dec.keyDecodingStrategy = .convertFromSnakeCase
        return dec
    }
    
    public func plants() async throws -> [Plant] {
        let request = HTTPClientRequest(url: baseUrl.append(path: "/api/v1/plants/list"))
        let response = try await client.execute(request: request)
        
        let body = try await response.body.collect(upTo: 1024 * 1024)
        
        let plants = try JSONDecoder().decode([Plant.self], from: body)
        
        return plants
    }
    
    public func quote(plant: Components.Schemas.Plant) async throws -> String {
        ""
    }
}
