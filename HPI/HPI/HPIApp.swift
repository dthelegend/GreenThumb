//
//  HPIApp.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

@main
struct HPIApp: App {
    var body: some Scene {
        WindowGroup {
            Router()
                .environmentObject(APIEnvironment(isReal: true))
                .withErrorHandling()
        }
    }
}
