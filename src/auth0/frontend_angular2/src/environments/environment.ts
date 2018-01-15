// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.

export const environment = {
  production: false,
  JWT_AUTH_HEADER_PREFIX: 'JWT',
  auth0: {
    // client
    clientID: 'SfrzkiBBTmMnjS25roizCrJO3PbwDB3E',
    domain: 'dry-play.auth0.com',
    callbackURL: 'http://localhost:4200',
    // api
    audience: 'https://dry-play-api1.com',
  },
};
