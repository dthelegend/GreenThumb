//
//  Router.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

struct Router: View {
    var body: some View {
        NavigationStack {
            PlantsScreen()
                .navigationDestination(for: NavigationDestination.self) { destination in
                    switch destination {
                    case .plantDetailScreen(let plant):
                        PlantDetailScreen(plant: plant)
                    }
                }
        }
    }
}

#Preview {
    Router()
        .environment(APIEnvironment(isReal: false))
}
