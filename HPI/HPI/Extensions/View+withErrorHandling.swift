//
//  View+withErrorHandling.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import SwiftUI

struct HandleErrorsByShowingAlertViewModifier: ViewModifier {
    @State var errorHandling = ErrorHandling()

    func body(content: Content) -> some View {
        content
            .environment(errorHandling)
            .background(
                EmptyView()
                    .alert(
                        "Error",
                        isPresented: $errorHandling.isPresenting
                    ) {}
                message: {
                    Text(errorHandling.currentAlert?.message ?? "Unknown")
                }
            )
    }
}

extension View {
    func withErrorHandling() -> some View {
        modifier(HandleErrorsByShowingAlertViewModifier())
    }
}
