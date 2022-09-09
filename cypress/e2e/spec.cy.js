var test_url = 'http://192.168.64.3:10000/'

var test_submission = {
  "agency":"DOC/NIST",
  "system_owner":"Owner, System",
  "assessor":"Or, Assess",
  "software_admin":"Admin, Software",
  "acquisition_officer":"Officer, Acq",
  "agency_aws_account_id":"123456"
}

var ui_content = {
  "submit_button":"Request Enrollment",
  "rules_of_behavior_label":"Rules Of Behavior",
  "success_heading":"Your enrollment has been submitted."
}

describe('The Enrollment Dashboard', () => {
  it('is running.', () => {
    cy.visit(test_url)
  });

  it('can submit and enrollment request.', () => {
    cy.visit(test_url)

    cy.get('#agency').type(test_submission.agency)
    cy.get('#system_owner').type(test_submission.system_owner)
    cy.get('#assessor').type(test_submission.assessor)
    cy.get('#software_admin').type(test_submission.software_admin)
    cy.get('#acquisition_officer').type(test_submission.acquisition_officer)
    cy.get('#agency_aws_account_id').type(test_submission.agency_aws_account_id)

    cy.contains(ui_content.rules_of_behavior_label).click()
    cy.contains(ui_content.submit_button).click()

    cy.get('h2').should('contain', ui_content.success_heading)
  });

  it('handles the submitted request.', () => {
    cy.get('h2').should('contain', ui_content.success_heading)

    cy.get('.grid-container').should('contain', `Agency: ${test_submission.agency}`)
    cy.get('.grid-container').should('contain', `System Owner: ${test_submission.system_owner}`)
    cy.get('.grid-container').should('contain', `Assessor: ${test_submission.assessor}`)
    cy.get('.grid-container').should('contain', `Software Administrator: ${test_submission.software_admin}`)
    cy.get('.grid-container').should('contain', `Acquisition Officer: ${test_submission.acquisition_officer}`)
    cy.get('.grid-container').should('contain', `AWS Account Association: ${test_submission.agency_aws_account_id}`)
    cy.get('.grid-container').should('contain', 'Rules of Behavior: y')
  })
})