//
//  Plant.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import Foundation

struct Plant: Codable, Hashable, Identifiable {
    var id: Int
    
    let name: String
    let description: String
    let baseWaterLevel: Int
    let waterMin: Int
    let waterMax: Int
    let lightRequirment: Int
    let minTemperature: Int
    let maxTemperature: Int
    let minHumididty: Int
    let maxHumididty: Int
    let latestData: LatestData?
    
    //    {
    //      "name": "string",
    //      "description": "string",
    //      "base_water_level": 0,
    //      "water_min": 0,
    //      "water_max": 0,
    //      "light_requirment": 0,
    //      "min_temperature": 0,
    //      "max_temperature": 0,
    //      "min_humididty": 0,
    //      "max_humididty": 0,
    //      "id": 0,
    //      "latest_data": {
    //        "temperature": 0,
    //        "humidity": 0,
    //        "light_level": 0,
    //        "water_level": 0
    //      }
    //    }
}
