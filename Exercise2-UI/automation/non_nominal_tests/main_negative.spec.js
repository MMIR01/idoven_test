import { error_messages,
         invalid_url,
         long_url,
         waiting_result_text,
         website_speed_url } from "../variables";

describe('Speed Test Website Non-Nominal', () => {
    // Before each test, go back to the main page
    beforeEach(() => {
        cy.visit(website_speed_url);
    });

    it('should not allow starting the test with an empty URL', () => {
        // Try clicking Start Test without entering a URL
        cy.get('button').contains('Start Test').click();
        // Verify that the error message for empty URL is displayed
        cy.contains(error_messages.empty_url).should('be.visible');
    });

    it('should not allow starting the test with an invalid URL', () => {
        // Enter an invalid URL
        cy.get('input[name="url"]').type(invalid_url);
        cy.get('button').contains('Start Test').click();
        // Check if an error message appears
        cy.contains(error_messages.invalid_url).should('be.visible');
    });

    it('should allow long URLs', () => {
        // Enter a long URL
        cy.get('input[name="url"]').type(long_url);
        cy.get('button').contains('Start Test').click();
        // The test starts running but we don't need to wait until the end
        cy.contains(waiting_result_text).should('be.visible');
    });
});