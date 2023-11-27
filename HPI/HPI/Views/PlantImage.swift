//
//  PlantImage.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

struct PlantImage: View {
    let plant: Components.Schemas.PlantList
    
    var body: some View {
        Image(.plant)
            .resizable()
    }
}

#Preview {
    PlantImage(plant: .mock)
}
