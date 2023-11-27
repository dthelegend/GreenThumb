//
//  MockPlantAPI.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import Foundation

@Observable
class MockPlantAPI: PlantAPI {
    func plants() async throws -> [Components.Schemas.PlantList] {
        [.mock]
    }
    
    func quote(plant: Components.Schemas.Plant) async throws -> String {
        "Where my water at⁉️"
    }
}
