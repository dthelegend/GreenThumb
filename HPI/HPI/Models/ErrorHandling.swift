//
//  ErrorHandling.swift
//  HPI
//
//  Created by James on 25/11/2023.
//

import Foundation

struct ErrorAlert: Identifiable {
    var id = UUID()
    var message: String
    var dismissAction: (() -> Void)?
}

@Observable
class ErrorHandling {
    var currentAlert: ErrorAlert?
    var isPresenting = false

    func handle(error: Error) {
        currentAlert = ErrorAlert(message: error.localizedDescription)
        isPresenting = true
    }
}
