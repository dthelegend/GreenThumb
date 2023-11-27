//
//  APIEnvironment.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import Foundation

@Observable
class APIEnvironment: ObservableObject {
    let api: PlantAPI
    
    init(isReal: Bool) {
        if isReal {
            api = RealPlantAPI()
        } else {
            api = MockPlantAPI()
        }
    }
}
