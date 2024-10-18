import { website_speed_url,
         history_url,
         performance_overall,
         website_speed_elements } from '../variables.js';

describe('Website Speed Test Main', () => {
    // Before each test, go back to the main page
    beforeEach(() => {
        cy.visit(website_speed_url);
    });
    
    afterEach(() => {
        cy.screenshot()
    });

    it('should display main elements in the webpage', () => {
        // The GUI needs to have the main elements
        // Input text to write the url
        cy.get(website_speed_elements.input_field).should('be.visible');
        // Button to start the test
        cy.get('button').contains(website_speed_elements.start_test_text).should('be.visible');
        // Select to choose the device
        cy.get(website_speed_elements.device_select).should('be.visible');
        // Two options: mobile and desktop
        cy.get(website_speed_elements.device_select).find('option').should(($options) => {
            expect($options).to.have.length(3);
            expect($options.eq(0)).to.contain(website_speed_elements.mobile_option);
            expect($options.eq(1)).to.contain(website_speed_elements.desktop_option);
            expect($options.eq(2)).to.contain(website_speed_elements.sign_up_option);
        });

        // Link to test history
        cy.get(website_speed_elements.test_history_link)
        .contains(website_speed_elements.test_history_text).should('be.visible');
        //Link to view sample report
        cy.get(website_speed_elements.view_sample_report_link)
        .contains(website_speed_elements.view_sample_report_text).should('be.visible');
    });

    it('should be possible to go to the test history page', () => {
        // Click on the test history link
        cy.get(website_speed_elements.test_history_link)
        .contains(website_speed_elements.test_history_text).click();
        // Check if the URL is correct
        cy.url().should('include', history_url);
    });

    it('should be possible to go to the sample report page', () => {
        // Click on the view sample report link
        cy.get(website_speed_elements.view_sample_report_link)
        .contains(website_speed_elements.view_sample_report_text)
        .invoke('removeAttr', 'target') //this is the only way to handle new tabs in Cypres
        .click();
        // Verify that the sample report is loaded (it has the same title as the results page)
        cy.contains(performance_overall.page_title_text).should('be.visible');
    });
  });
  