//
//  MockPlant.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import Foundation

extension Plant {
    static var mock: Self {
//        .init(
//            id: 1,
//            name: "花ちゃん",
//            imageUrl: URL(string: "https://example.com")!
//        )
//        .init(
//            name: "花ちゃん",
//            description: "花ちゃんはもっとかわいい花だ！",
//            id: 1)
        .init(
            name: "花ちゃん",
            description: "花ちゃんはもっとかわいい花だ！",
            base_water_level: 100,
            water_min: 100,
            water_max: 800,
            light_requirment: 300,
            min_temperature: 15,
            max_temperature: 30,
            min_humididty: 20,
            max_humididty: 60,
            id: 1)
    }
}
