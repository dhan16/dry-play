interface AuthConfig {
  clientID: string;
  domain: string;
  callbackURL: string;  // also used as logoutReturnToURL
  audience: string;
}

export const AUTH_CONFIG: AuthConfig = {
  clientID: 'LejDX0O6TCLHmpj6tM9CeufbIlhsbXsv',
  domain: 'dhan16.eu.auth0.com',
  callbackURL: 'http://localhost:4200',
  audience: 'https://dhan16-api1.com',
};
