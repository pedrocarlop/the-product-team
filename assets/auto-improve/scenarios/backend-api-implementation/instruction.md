# Scenario: Backend API Implementation

## Task
Design a REST API for a multi-tenant workspace management system. The system allows organizations to create workspaces, invite members with role-based permissions, and manage workspace settings. Each tenant is an organization that can have multiple workspaces.

## Requirements
1. **Resource Model**: Define the core resources (Organization, Workspace, Member, Invitation) with their attributes, relationships, and constraints. Use a clear schema notation.
2. **Endpoints**: Specify at least 15 endpoints covering CRUD operations, membership management, and workspace settings. Include HTTP method, path, request/response schemas, and status codes.
3. **Auth Scheme**: Describe the authentication (API keys, OAuth2, or JWT) and authorization model. Explain how tenant isolation is enforced at the API layer.
4. **Error Handling**: Define a consistent error response format with error codes, messages, and a catalog of at least 10 domain-specific error types.
5. **Pagination**: Specify the pagination strategy (cursor-based or offset-based) with request parameters and response envelope format. Include sorting and filtering conventions.

## Output Contract
Produce a `api-design.md` artifact with ## sections for each requirement. Use code blocks for request/response examples and tables for endpoint listings.
