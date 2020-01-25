module.exports = {
  "assetsDir": "assets",
  "publicPath": "/",
  "pages": {
    "styles": {
      "entry": "src/styles.js",
      "template": "public/index.html",
      "filename": "index.html",
      "chunks": [
        "chunk-vendors",
        "chunk-common",
        "styles"
      ]
    },
    "home": {
      "entry": "src/pages/home/main.js",
      "template": "public/index.html",
      "filename": "home/index.html",
      "title": "Home",
      "chunks": [
        "chunk-vendors",
        "chunk-common",
        "styles",
        "home"
      ]
    },
    "events": {
      "entry": "src/pages/events/main.js",
      "template": "public/index.html",
      "filename": "events/index.html",
      "title": "Events",
      "chunks": [
        "chunk-vendors",
        "chunk-common",
        "styles",
        "events"
      ]
    },
    "projects": {
      "entry": "src/pages/projects/main.js",
      "template": "public/index.html",
      "filename": "projects/index.html",
      "title": "Projects",
      "chunks": [
        "chunk-vendors",
        "chunk-common",
        "styles",
        "projects"
      ]
    }
  },
  "pwa": {
    "name": "Sam Scheding",
    "themeColor": "#00c2da",
    "msTileColor": "#00c2da",
    "appleMobileWebAppCapable": "yes",
    "appleMobileWebAppStatusBarStyle": "default",
    "iconPaths": {
      "favicon32": "public/favicon.ico",
      "favicon16": "public/favicon.ico",
      "appleTouchIcon": "public/favicon.ico",
      "maskIcon": "public/favicon.ico",
      "msTileImage": "public/favicon.ico"
    }
  },
  "configureWebpack": {
    "resolve": {
      "alias": {
        "@component-library": "/Users/SamTheNormalOne/projects/www.scheding.com.au/fe/component-library"
      }
    },
    "performance": {
      "hints": false
    },
    "plugins": []
  },
  "css": {
    "loaderOptions": {
      "sass": {
        "includePaths": [
          "../"
        ]
      }
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}