//
//  PlantListTile.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

struct PlantListTile: View {
    let plant: Components.Schemas.PlantList
    
    var body: some View {
        HStack {
            PlantImage(plant: plant)
                .frame(width: 44, height: 44)
                .clipShape(.rect(cornerRadius: 8))
            VStack(alignment: .leading) {
                Text(plant.name)
                Text(plant.description)
                    .foregroundStyle(.secondary)
            }
        }
    }
}

#Preview {
    PlantListTile(plant: .mock)
}
