//
//  PlantAPI.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import Foundation

protocol PlantAPI {
    func plants() async throws -> [Components.Schemas.PlantList]
    
    func quote(plant: Components.Schemas.Plant) async throws -> String
}
