import { history_url, 
         test_history_page, 
         performance_overall,
         url_speed_test,
         waiting_result_text,
         website_speed_elements,
         website_speed_url } from "../variables";

describe('Test History Page', () => {
    it('should print empty history message', () => {
        cy.visit(history_url);
        cy.contains(test_history_page.empty);
    });

    it('should load the page successfully', () => {
        // Run a test
        cy.visit(website_speed_url);
        // Check if the input field and button are present
        cy.get(website_speed_elements.input_field).should('be.visible');
        cy.get('button').contains(website_speed_elements.start_test_text).should('be.visible');
        // Type address to test
        cy.get(website_speed_elements.input_field).type(url_speed_test);
        // Select mobile device
        cy.get('select[name="device"]').select('mobile');
        // Click on start test
        cy.get('button').contains(website_speed_elements.start_test_text).click();
        cy.contains(waiting_result_text).should('be.visible');
        // Wait at least 5 minutes for the test to complete
        cy.contains(performance_overall.page_title_text, { timeout: 300000 });
        
        // Go to the test history page
        cy.get('a').contains('Test History').click();

        // Check page content
        cy.get('h1').should('contain', test_history_page.main_text);
        // Should display the history table'
        cy.get('table').should('be.visible');
        cy.get('table thead tr th').should('have.length', 3);
        // Assuming we have at least one test in the history
        cy.get('table tbody tr').should('have.length.greaterThan', 0);
        
        // Check table headers'
        cy.get('table thead tr th').eq(0).should('contain', test_history_page.url_section);
        cy.get('table thead tr th').eq(1).should('contain', test_history_page.device_section);
        cy.get('table thead tr th').eq(2).should('contain', test_history_page.date_section);
        
        // Check there is data in the table
        cy.get('table tbody tr').each(($row) => {
            cy.wrap($row).find('td').eq(0).should('not.be.empty'); // URL column
            cy.wrap($row).find('td').eq(1).should('not.be.empty'); // Date column
            cy.wrap($row).find('td').eq(2).should('not.be.empty'); // Device column
        });

        // Access to the report of the first test
        cy.get('table tbody tr').first().find('td').eq(0) // URL column, first row
        .find('a').eq(0).click(); // Click on the URL
        cy.contains(performance_overall.page_title_text);
    });
});