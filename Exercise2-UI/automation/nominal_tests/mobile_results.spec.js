import { performance_overall, 
         performance_lighthouse,
         performance_metrics_summary, 
         performance_metrics_vitals, 
         performance_other_results,
         performance_sections,
         website_speed_url,
         website_speed_elements,
         waiting_result_text,
         url_speed_test, 
         performance_lab_view} from "../variables";

describe('Mobile test results', () => {
  
    // As a test suite, we will run a test for the mobile device
    before(() => {    
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
        
        // For debugging purposes, comment out all above code and uncomment the following line
        //cy.visit('website-speed/Ek0mMTe0/');

        // Get current URL for the tests
        cy.url().then((url) => {
            Cypress.env('current_url', url);
        });
    });
    
    beforeEach(() => {
        cy.visit(Cypress.env('current_url'));
        // Wait until the page results are loaded
        cy.contains(performance_overall.page_title_text)
    });

    it('should display overall results after test completion', () => {
        // Check Overall results
        Object.entries(performance_overall).forEach(([key, value]) => {
            cy.contains(value).should('be.visible');
        });
    });

    it('should display performance metrics overview after test completion', () => {       
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

    it('should display performance metrics vitals after test completion', () => {
        cy.contains(performance_sections.web_vitals_text).click();
        Object.entries(performance_metrics_vitals).forEach(([key, value]) => {
            cy.contains(value).should('be.visible');
        });
    });

    it('should display requests info after test completion', () => {
        cy.contains(performance_sections.requests_text).click();
        cy.contains('Request Waterfall').should('be.visible');
    });

    it('should display lighthouse scores after test completion', () => {
        cy.contains(performance_sections.lighthouse_text).click();
        Object.entries(performance_lighthouse).forEach(([key, value]) => {
            cy.contains(value).should('be.visible');
        });
    });

    it('should display other useful info of the test results', () => {
        Object.entries(performance_other_results).forEach(([key, value]) => {
            cy.contains(value).should('be.visible');
        });
    });

    it('should be possible to run another test', () => {
        // Click on the button to run another test
        cy.get('a').contains('Run Another Test').click();
        // Check if the input field and button are present
        cy.get(website_speed_elements.input_field).should('be.visible');
        cy.get('button').contains(website_speed_elements.start_test_text).should('be.visible');
    });

    it('should be possible to view the test history', () => {
        // Click on the link to view the test history
        cy.get('a').contains('Test History').click();
        // Verify that the test history page is loaded
        cy.contains('Test History').should('be.visible');
    });
  });
  