//
//  LatestData.swift
//  HPI
//
//  Created by James on 26/11/2023.
//

import Foundation

struct LatestData: Codable, Hashable {
    let temperature: Int
    let humidity: Int
    let lightLevel: Int
    let waterLevel: Int
    //      "latest_data": {
    //        "temperature": 0,
    //        "humidity": 0,
    //        "light_level": 0,
    //        "water_level": 0
    //      }
    //    }
}
