//
//  PlantsScreen.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

struct PlantsScreen: View {
    @Environment(APIEnvironment.self) private var api
    @Environment(ErrorHandling.self) private var errorHandling
    
    @State private var plants: [Components.Schemas.PlantList] = []
    
    var body: some View {
        List(plants) { plant in
            NavigationLink(value: NavigationDestination.plantDetailScreen(plant)) {
                PlantListTile(plant: plant)
            }
        }
        .navigationTitle("Plants")
        .task {
            do {
                plants = try await api.api.plants()
            } catch {
                errorHandling.handle(error: error)
            }
        }
        .refreshable {
            do {
                plants = try await api.api.plants()
            } catch {
                errorHandling.handle(error: error)
            }
        }
    }
}

#Preview {
    NavigationStack {
        PlantsScreen()
            .environment(APIEnvironment(isReal: false))
            .withErrorHandling()
    }
}
