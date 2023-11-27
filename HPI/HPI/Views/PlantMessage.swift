//
//  PlantMessage.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

struct PlantMessage: View {
    @Environment(APIEnvironment.self) private var api
    @Environment(ErrorHandling.self) private var errorHandling
    @State private var optionalQuote: String?
    
    let plant: Components.Schemas.Plant
    
    private var quote: String {
        optionalQuote ?? "..."
    }
    
    
    var body: some View {
        Text("“\(quote)”")
            .font(.system(size: 26, weight: .semibold, design: .serif))
            .foregroundStyle(.opacity(0.9))
            .task {
                do {
                    optionalQuote = try await api.api.quote(plant: plant)
                } catch {
                    errorHandling.handle(error: error)
                }
            }
    }
}

#Preview {
    PlantMessage(plant: .mock)
        .environment(APIEnvironment(isReal: false))
        .withErrorHandling()
}
