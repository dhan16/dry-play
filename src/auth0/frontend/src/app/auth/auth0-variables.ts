interface AuthConfig {
  clientID: string;
  domain: string;
  callbackURL: string;
}

export const AUTH_CONFIG: AuthConfig = {
  clientID: 'LejDX0O6TCLHmpj6tM9CeufbIlhsbXsv',
  domain: 'dhan16.eu.auth0.com',
  callbackURL: 'http://localhost:4200/callback'
};
