import { performance_overall, 
         performance_metrics_summary, 
         website_speed_url,
         website_speed_elements,
         performance_lab_view} from "../variables";

describe('Sample Report Page', () => {
  
    // As a test suite, we will run a test for the mobile device
    beforeEach(() => {    
        cy.visit(website_speed_url);

        // Click on the view sample report link
        cy.get(website_speed_elements.view_sample_report_link)
        .contains(website_speed_elements.view_sample_report_text)
        .invoke('removeAttr', 'target') //this is the only way to handle new tabs in Cypres
        .click();
        // Verify that the sample report is loaded (it has the same title as the results page)
        cy.contains(performance_overall.page_title_text).should('be.visible');

        // Get current URL for the tests
        cy.url().then((url) => {
            Cypress.env('current_url', url);
        });
    });
    
    it('should show a sample report', () => {
        // Check Overall results
        Object.entries(performance_overall).forEach(([key, value]) => {
            cy.contains(value).should('be.visible');
        });

        // Check Lab View Section
        Object.entries(performance_lab_view).forEach(([key, value]) => {
            cy.contains(value).should('be.visible');
        });

        // Check Summary Section
        cy.get('[data-test-filter-button]').contains('Summary').click();
        Object.entries(performance_metrics_summary).forEach(([key, value]) => {
            cy.contains(value).should('be.visible');
        });
    });
  });
  