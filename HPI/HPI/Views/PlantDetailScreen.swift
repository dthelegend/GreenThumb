//
//  PlantDetailScreen.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

struct PlantDetailScreen: View {
    let plant: Components.Schemas.PlantList
    
    var body: some View {
        ScrollView {
            PlantImage(plant: .mock)
                .aspectRatio(contentMode: .fit)
                .clipShape(.rect(cornerRadius: 24))
                .padding()
            PlantMessage(plant: plant)
        }
        .navigationTitle(plant.name)
        
    }
}

#Preview {
    NavigationStack {
        PlantDetailScreen(plant: .mock)
    }
}
