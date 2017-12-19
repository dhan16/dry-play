interface AuthConfig {
  clientID: string;
  domain: string;
  callbackURL: string;  // also used as logoutReturnToURL
  audience: string;
}

export const AUTH_CONFIG: AuthConfig = {
  clientID: 'SfrzkiBBTmMnjS25roizCrJO3PbwDB3E',
  domain: 'dry-play.auth0.com',
  callbackURL: 'http://localhost:4200',
  audience: 'https://dry-play-api1.com',
};
