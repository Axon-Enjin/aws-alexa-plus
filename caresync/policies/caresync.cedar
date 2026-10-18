// CareSync execution boundary.
// Reads and proposals are allowed for the designated caregiver when consent
// is on file. Execution (a device reminder, a wallet charge) is forbidden
// unless that same caregiver has confirmed the specific staged action.
//
// This is the policy a Bedrock AgentCore Policy deploy would load.
// The demo enforces the same three rules in process so it runs locally.

permit (
  principal,
  action == CareSync::Action::"read",
  resource
)
when { context.consent == true && context.role == "caregiver" };

permit (
  principal,
  action == CareSync::Action::"propose",
  resource
)
when { context.consent == true && context.role == "caregiver" };

forbid (
  principal,
  action == CareSync::Action::"execute",
  resource
)
unless {
  context.confirmed == true &&
  context.role == "caregiver" &&
  context.consent == true
};
