from html_parsing_tools import html_parsing_tools
from sympy import false

html = """
<html dir="ltr" lang="en" class="no-applicationcache cookies dataview history postmessage svg websockets localstorage sessionstorage websqldatabase webworkers hashchange audio canvas canvastext video webgl csscalc cssgradients multiplebgs opacity rgba hsla supports fontface generatedcontent textshadow cssanimations bgrepeatround bgrepeatspace backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy cssreflections csstransforms csstransforms3d csstransitions fullscreen indexeddb translated-ltr indexeddb-deletedatabase"><plasmo-csui></plasmo-csui><head>

<meta charset="utf-8">
<!-- 
	This website is powered by TYPO3 - inspiring people to share!
	TYPO3 is a free open source Content Management Framework initially created by Kasper Skaarhoj and licensed under GNU/GPL.
	TYPO3 is copyright 1998-2023 of Kasper Skaarhoj. Extensions are copyright of their respective owners.
	Information and contribution at https://typo3.org/
-->


<link rel="shortcut icon" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/favicon.ico" type="image/vnd.microsoft.icon">

<meta name="generator" content="TYPO3 CMS">
<meta name="description" content="Photovoltaik – Beratung, Planung u. Montage von Photovoltaik Anlagen (PV) und Stromspeicher. Einspeisevergütung,  Förderungen &amp; Wirtschaftlichkeit.">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="author" content="Enerix">
<meta name="robots" content="all">
<meta name="keywords" content="Photovoltaik">
<meta property="og:title" content="Photovoltaik – Beratung, Planung u. Montage von Photovoltaik Anlagen (PV) und Stromspeicher. Einspeisevergütung, Förderungen &amp;amp; Wirtschaftlichkeit.">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:url" content="https://www.enerix.de/">
<meta property="og:image" content="https://www.enerix.de/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/mstile-144x144.png">
<meta name="twitter:card" content="summary">
<meta name="twitter:image" content="https://www.enerix.de/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/mstile-144x144.png">
<meta name="copyright" content="Enerix">
<meta name="revisit-after" content="7 days">
<meta name="google-site-verification" content="Sbau_Xwi57D8J04FHsHoBl6b6AJEVqCTsINbf3USsQk">
<meta name="p:domain_verify" content="6760e4f70dcbd31cf18c4d027fde919c">

<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/bootstrap.min-e4a14c741513a237dcb31cd169282655.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/jquery-ui.min-33dd177d26c75a478612b47083a9c755.css.1660289911.gzip" media="all">

<link rel="stylesheet" type="text/css" href="/typo3conf/ext/enerix/Resources/Public/Extensions/tx_news/Public/Css/news-basic.1659531846.css" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/93023019f2-e38daeff366c4de8a8a507cc9645b53d.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/struktur-83be979b4c465a2ce74a5245c15c755e.css.1683100635.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/navigation-693485d07ec9f89bbed90b13c81e8e4a.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/font-a3b4a1c9f60d39095bb74fa162925cfc.css.1668582897.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/fontawesome.min-96e2088416404d1044833dba1544cf47.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/extensions-c17f66a74dc6edfd74edf097e143f2d4.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/photoswipe-0a56fce1e486ce45ba4d554174771990.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/default-skin-ad110291185278a2adf1af37aa934472.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/responsive-0ad9a5ba18394d9c738566bef4e4f892.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/sections-b716c01fa6cd346632e672360701d2a9.css.1661498100.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/content-1223efcb53e56639748c0d3e19cb0371.css.1669799193.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/Main.min-ece3dcc310c7e2a1c4dccc5342198288.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/Basic-2b7d3f35c310958f1ba948850b55c523.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/dp_cookieconsent-672c86ce11ea31fe6d26b8ab7f807db0.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/feusersmap-50cd25a6db5a18c4d1761492bb9ffc29.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/landingpage-827491eaf98df0a05ae19f38f74d9302.css.1661853588.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/Additional.min-2b2f8a1c297a0adb6d88af9800604001.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/main-d41683d48295efe6c90dac550a787171.css.1660289911.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/shariff.min-7abda02dec35b4bd51ae9cfb10f56f82.css.1660290007.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/enerix-4fd203e7b31558894699e65e95aff006.css.1669799081.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/additional-0e05a6d8cd5d0f8c9e1d289d7206b97d.css.1666256571.gzip" media="all">
<link rel="stylesheet" type="text/css" href="/typo3temp/assets/compressed/hnm_fix-95a5e2e589c399b45c14f107d3f02eea.css.1666256256.gzip" media="all">



<script src="/typo3temp/assets/compressed/merged-24df23ea1f4c737029bf53956bcf4e0e-822981d86f134ab0a1462764ff85a2de.js.1684138650.gzip"></script>
<script src="/typo3conf/ext/enerix/Resources/Public/Javascript/jquery.min.1616063702.js"></script>
<script src="/typo3conf/ext/enerix/Resources/Public/Javascript/jquery-ui.min.1573120528.js"></script>

<script src="/typo3temp/assets/compressed/merged-07efbc13069c721d9d1ec1973a045f07-49ecc20048129591f49c4adb04bd2479.js.1660289911.gzip"></script>



<title>Enerix - Photovoltaik - Vorteile, Kosten und Förderungen</title>
        <link rel="apple-touch-icon" sizes="57x57" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-57x57.png">
        <link rel="apple-touch-icon" sizes="60x60" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-60x60.png">
        <link rel="apple-touch-icon" sizes="72x72" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="76x76" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-76x76.png">
        <link rel="apple-touch-icon" sizes="114x114" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-114x114.png">
        <link rel="apple-touch-icon" sizes="120x120" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-120x120.png">
        <link rel="apple-touch-icon" sizes="144x144" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-144x144.png">
        <link rel="apple-touch-icon" sizes="152x152" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-152x152.png">
        <link rel="apple-touch-icon" sizes="180x180" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/apple-touch-icon-180x180.png">
        <link rel="icon" type="image/png" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/favicon-32x32.png" sizes="32x32">
        <link rel="icon" type="image/png" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/favicon-194x194.png" sizes="194x194">
        <link rel="icon" type="image/png" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/favicon-96x96.png" sizes="96x96">
        <link rel="icon" type="image/png" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/android-chrome-192x192.png" sizes="192x192">
        <link rel="icon" type="image/png" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/favicon-16x16.png" sizes="16x16">
        <link rel="manifest" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/manifest.json">
        <link rel="mask-icon" href="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/safari-pinned-tab.svg">
        <meta name="apple-mobile-web-app-title" content="Enerix Franchise">
        <meta name="application-name" content="Enerix Franchise">
        <meta name="msapplication-TileColor" content="#da532c">
        <meta name="msapplication-TileImage" content="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/mstile-144x144.png">
        <meta name="msapplication-config" content="/typo3conf/ext/enerix/Resources/Public/Icons/Favicons/browserconfig.xml">
        <meta name="theme-color" content="#ffffff">
        <meta name="p:domain_verify" content="6760e4f70dcbd31cf18c4d027fde919c">
        <meta name="google-site-verification" content="Sbau_Xwi57D8J04FHsHoBl6b6AJEVqCTsINbf3USsQk">
<link rel="preload" href="/typo3conf/ext/enerix/Resources/Public/Css/font.css" as="font"><script data-ignore="1" data-cookieconsent="statistics" type="text/plain"></script>

<script type="text/plain" data-ignore="1" data-dp-cookiedesc="layout">
    Diese Website benutzt Cookies, die für den technischen Betrieb der Website erforderlich sind und stets gesetzt werden. Andere Cookies, um Inhalte und Anzeigen zu personalisieren und die Zugriffe auf unsere Website zu analysieren, werden nur mit Ihrer Zustimmung gesetzt. Außerdem geben wir Informationen zu Ihrer Verwendung unserer Website an unsere Partner für soziale Medien, Werbung und Analysen weiter.



</script>
<script type="text/plain" data-ignore="1" data-dp-cookieselect="layout">
    <div class="dp--cookie-check" xmlns:f="http://www.w3.org/1999/html">
    <label for="dp--cookie-require">
        <input type="hidden" name="" value="" /><input disabled="disabled" class="dp--check-box" id="dp--cookie-require" tabindex="-1" type="checkbox" name="" value="" checked="checked" />
        Notwendig
    </label>
    <label for="dp--cookie-statistics">
        <input class="dp--check-box" id="dp--cookie-statistics" tabindex="1" type="checkbox" name="" value="" checked="checked" />
        Statistiken
    </label>
    <label for="dp--cookie-marketing">
        <input class="dp--check-box" id="dp--cookie-marketing" tabindex="1" type="checkbox" name="" value="" checked="checked" />
        Marketing
    </label>
</div>

</script>
<script type="text/plain" data-ignore="1" data-dp-cookierevoke="layout">
    <div class="cc-revoke dp--revoke {{classes}}">
    <i class="dp--icon-fingerprint"></i>
    <span class="dp--hover">Cookies</span>
</div>



</script>
<script type="text/plain" data-ignore="1" data-dp-cookieiframe="layout">
    <div class="dp--overlay-inner">
    <div class="dp--overlay-header">{{notice}}</div>
    <div class="dp--overlay-description">{{desc}}</div>
    <div class="dp--overlay-button">
        <button class="db--overlay-submit" onclick="window.DPCookieConsent.forceAccept(this)" data-cookieconsent="{{type}}" >
        {{btn}}
        </button>
    </div>
</div>

</script>
<script type="text/javascript" data-ignore="1">
    window.cookieconsent_options = {
        overlay: {
            notice: true,
            box: {
                background: 'rgba(255,255,255,.97)',
                text: '#7d7d7d'
            },
            btn: {
                background: '#b81839',
                text: '#fff'
            }
        },
        content: {
            message:'Diese Website benutzt Cookies, die für den technischen Betrieb der Website erforderlich sind und stets gesetzt werden. Andere Cookies, um Inhalte und Anzeigen zu personalisieren und die Zugriffe auf unsere Website zu analysieren, werden nur mit Ihrer Zustimmung gesetzt. Außerdem geben wir Informationen zu Ihrer Verwendung unserer Website an unsere Partner für soziale Medien, Werbung und Analysen weiter.',
            dismiss:'Cookies zulassen!',
            allow:'Speichern',
            deny: 'Ablehnen',
            link:'Mehr Infos',
            href:'/',
            target:'_blank',
            'allow-all': 'alle akzeptieren!',

            media: {
                notice: 'Cookie-Hinweis',
                desc: 'Durch das Laden dieser Ressource wird eine Verbindung zu externen Servern hergestellt, die Cookies und andere Tracking-Technologien verwenden, um die Benutzererfahrung zu personalisieren und zu verbessern. Weitere Informationen finden Sie in unserer Datenschutzerklärung.',
                btn: 'Erlaube Cookies und lade diese Ressource',
            }
        },
        theme: 'edgeless',
        position: 'bottom-left',
        type: 'opt-in',
        revokable: true,
        reloadOnRevoke: true,
        checkboxes: {"statistics":"true","marketing":"true"},
        palette: {
            popup: {
                background: 'rgba(255,255,255,.97)',
                text: '#7d7d7d'
            },
            button: {
                background: '#a3d20b',
                text: '#fff',
            }
        }
    };
</script>


	<!-- Google Tag Manager -->
	<script data-ignore="1" data-cookieconsent="statistics" type="text/plain">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KHJZR5Z');</script>
	<!-- End Google Tag Manager -->	<!-- Google Analytics -->
    <script data-ignore="1" data-cookieconsent="statistics" data-src="https://www.googletagmanager.com/gtag/js?id=UA-17911350-1"></script>
    <script data-ignore="1" data-cookieconsent="statistics" type="text/plain">
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
    	gtag('js', new Date());
    	gtag('config', 'UA-17911350-1', { 'anonymize_ip': true });
    </script>	<script type="text/javascript" src="https://klicktipp.s3.amazonaws.com/listbuildings/system/forms/scripts/protect.js"></script>
<link rel="canonical" href="https://www.enerix.de/">


<link type="text/css" rel="stylesheet" href="https://www.provenexpert.com/css/widget_landing.css"><link type="text/css" rel="stylesheet" href="https://www.provenexpert.com/css/google-stars.css"><link type="text/css" rel="stylesheet" charset="UTF-8" href="https://www.gstatic.com/_/translate_http/_/ss/k=translate_http.tr.69JJaQ5G5xA.L.W.O/d=0/rs=AN8SPfpC36MIoWPngdVwZ4RUzeJYZaC7rg/m=el_main_css"><style class="automa-element-selector">@font-face { font-family: "Inter var"; font-weight: 100 900; font-display: swap; font-style: normal; font-named-instance: "Regular"; src: url("chrome-extension://infppggnoaenmfagbfknfkancpbljcca/Inter-roman-latin.var.woff2") format("woff2") }
.automa-element-selector { direction: ltr } 
 [automa-isDragging] { user-select: none } 
 [automa-el-list] {outline: 2px dashed #6366f1;}</style></head>
<body id="default" class="p37 dp--cookie-consent"><a name="top" id="top-position"></a>



        <h2 class="aural"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Enerix</font></font></h2><p class="navSkip"><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Jump directly to:</font></font></em></p><ul class="navSkip"><a class="sr-only sr-only-focusable" href="#content"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Go to content</font></font></a><a class="sr-only sr-only-focusable" href="#hauptmenue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">To the main navigation</font></font></a><a class="sr-only sr-only-focusable" href="#footer"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">To the footer</font></font></a></ul><a id="top-position" aria-hidden="true"></a><div id="wrapper"><div id="page" class="overflow-x-hidden container-fluid px-0"><header class="defaultHeader"><div class="quickContact w-100"><div class="container"><div class="row position-relative"><div class="col-xl-7 col-lg-12 contact-bar"><div itemscope="" itemtype="http://schema.org/Corporation"><a href="/kontakt/" title="email to enerix" class="sr-only"><span itemprop="email"><i class="fas fa-envelope red-badge"></i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">info@enerix.de
                                </font></font></span></a><a href="tel:+498007992000" title="call Enerix"><span itemprop="telephone"><i class="fas fa-phone-alt red-badge"></i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">0 800 7992 000
                                </font></font></span></a><a title="Contact" href="https://www.enerix.de/kontakt-1"><i class="fa fa-arrow-right red-badge"></i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contact
                        </font></font></a><a href="/service/photovoltaik-leitfaden/" title="Free guide"><i class="fa fa-book red-badge"></i><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Free guide
                            </font></font></a></div></div><div class="col-xl-5 col-lg-12 px-0"><div id="localPartnersForm" class="me-lg-2"><div class="gradient"></div><div class="partnerFormHeader px-3 py-1"><span class="d-inline-block pe-3 pt-1 align-top"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Your local partner</font></font></span><span class="d-inline-block"><div id="c657" class="frame frame-default frame-type-list frame-layout-0"><div class="tx-femanager" data-labels="{&quot;loading_states&quot;:&quot;Lade Bundesl\u00e4nder ...&quot;,&quot;please_choose&quot;:&quot;Bitte w\u00e4hlen...&quot;}">
	

    <div class="femanager_list">
        


        

    <div class="femanager_list_searchform">
        <form name="filter" class="form-inline mt-1 mb-1" action="/?tx_femanager_pi1%5Bcontroller%5D=User&amp;cHash=390abfb671b119f69c9efba9ea08af92" method="post">
<div>
<input type="hidden" name="tx_femanager_pi1[__referrer][@extension]" value="Femanager">
<input type="hidden" name="tx_femanager_pi1[__referrer][@controller]" value="User">
<input type="hidden" name="tx_femanager_pi1[__referrer][@action]" value="list">
<input type="hidden" name="tx_femanager_pi1[__referrer][arguments]" value="YTowOnt989b841f7f445b3b389b13cdb3740872636e1a6fd">
<input type="hidden" name="tx_femanager_pi1[__referrer][@request]" value="{&quot;@extension&quot;:&quot;Femanager&quot;,&quot;@controller&quot;:&quot;User&quot;,&quot;@action&quot;:&quot;list&quot;}f86397eaaf8d27409752e914488601abc6c51142">
<input type="hidden" name="tx_femanager_pi1[__trustedProperties]" value="{&quot;filter&quot;:{&quot;searchword&quot;:1},&quot;buttonName&quot;:1}c3bd4d3c012d4d9d10b3305d165a84c0beb55d0b">
</div>

            <div class="femanager_fieldset femanager_city input-group">
                <label for="searchword" class="sr-only"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Postcode</font></font></label>
                <input size="10" placeholder="Postcode" pattern=".{5,}" class="form-control w-50" id="searchword" type="text" name="tx_femanager_pi1[filter][searchword]">

                <span class="input-group-btn">
                    <button class="btn btn-success rounded-0" type="submit" name="tx_femanager_pi1[buttonName]" value="buttonValue"><span class="fa fa-search"></span></button>
                </span>
            </div>
        </form>
    </div>



        

            
    </div>



	<div class="d-none invisible hidden">
    
    <input type="hidden" id="femanagerLanguage" value="0">

    
    <input type="hidden" id="femanagerStoragePid" value="83">

    
    <input type="hidden" id="femanagerPid" value="37">

    
    <input type="hidden" id="uploadFolder" value="">

    
    <input type="hidden" id="uploadAmount" value="3">

    
    <input type="hidden" id="uploadSize" value="25000000">

    
    <input type="hidden" id="uploadFileExtension" value="jpeg, jpg, gif, png, bmp, tif, tiff">

    
    <div class="femanager_validation_container">
        <div class="alert alert-error">
            <button type="button" class="close" data-dismiss="alert">×</button>
            Fehler
            
        </div>
    </div>
</div>
</div>
</div></span></div></div></div></div></div></div><div class="fix-on-scroll w-100"><div class="container"><nav class="navbar navbar-expand-lg navbar-inverse navbar-static-top" role="navigation"><div class="container-fluid px-0"><a class="navbar-brand ps-2" href="https://www.enerix.de/" title="Enerix® Franchise GmbH &amp; Co KG home page"><picture><img title="Enerix® Franchise GmbH &amp; Co KG" alt="Enerix® Franchise GmbH &amp; Co KG" src="/typo3conf/ext/enerix/Resources/Public/Images/enerix_logo.png" width="180" height="81"></picture></a><button type="button" class="navbar-toggler me-2" data-bs-toggle="offcanvas" data-bs-target="#navigation" data-bs-target-2=".side-collapse-container"><i class="fa-solid fa-bars"></i></button><div class="collapse navbar-collapse offcanvas offcanvas-end" tabindex="-1" id="navigation"><div class="offcanvas-header"><img title="Enerix® Franchise GmbH &amp; Co KG" alt="Enerix® Franchise GmbH &amp; Co KG" src="/typo3conf/ext/enerix/Resources/Public/Images/enerix_logo.png" width="180" height="81"><button type="button" class="btn-close text-reset position-absolute top-0 end-0 m-0 p-4" data-bs-dismiss="offcanvas" aria-label="Close"></button></div><ul class="nav navbar-nav navbar-end ms-auto"><li class="hasSub dropdown "><a class="d-inline-block" title="Decentralized energy supply - self-sufficiency with solar" href="/produkte"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Products</font></font></a><a href="#" class="dropdown-toggle position-absolute" data-bs-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="true"><span class="caret"></span></a><ul class="dropdown-menu"><li class="sub  dropdown-submenu"><a href="/produkte/photovoltaikanlagen">Photovoltaikanlagen</a><ul class="dropdown-menu"><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/bauer-solar">Bauer Solartechnik</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/montagesysteme">Montagesysteme</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/sflex">S:FLEX</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/sun-ballast">Sun Ballast</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/photovoltaikmodule">Photovoltaikmodule</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/aleo">aleo</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/q-cells-module">Q Cells Module</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/heckert">Heckert</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/solarwatt">Solarwatt</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/solarfabrik">Solar Fabrik</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/fronius">Fronius</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/solaredge">Solaredge</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/eigenverbrauch">Eigenverbrauch</a></li><li class="  dropdown-submenu"><a href="/produkte/photovoltaikanlagen/sma">SMA</a></li></ul></li><li class="sub dropdown-submenu"><a href="/produkte/stromspeicher">Stromspeicher</a><ul class="dropdown-menu"><li class="  dropdown-submenu"><a href="/produkte/batteriespeicher">Batteriespeicher</a></li><li class="  dropdown-submenu"><a href="/produkte/stromspeicher/sicherheit">Sicherheit</a></li><li class="  dropdown-submenu"><a href="/produkte/stromspeicher/notstromversorgung">Notstromversorgung</a></li></ul></li><li class="sub dropdown-submenu"><a href="/produkte/stromcloud">Stromcloud</a><ul class="dropdown-menu"><li class="  dropdown-submenu"><a href="/produkte/stromcloud/sonnenflat-x">sonnenFlat X</a></li><li class="  dropdown-submenu"><a href="/produkte/stromcloud/seneccloud">Senec.Cloud</a></li></ul></li><li class="sub dropdown-submenu"><a href="/produkte/solarterrasse">Solarterrasse</a><ul class="dropdown-menu"><li class="  dropdown-submenu"><a href="/produkte/solarterrasse/esonne">esonne</a></li><li class="  dropdown-submenu"><a href="/produkte/solarterrasse/glasvordach">glasvordach</a></li></ul></li><li class="sub dropdown-submenu"><a href="/produkte/solarcarport">Solarcarport</a><ul class="dropdown-menu"><li class="  dropdown-submenu"><a href="/produkte/solarcarport/esonne">esonne</a></li><li class="  dropdown-submenu"><a href="/produkte/solarcarport/glasvordach">glasvordach</a></li></ul></li><li class=" dropdown-submenu"><a href="/produkte/wallbox">Wallbox</a></li><li class=" dropdown-submenu"><a href="/produkte/solarstrom-fuer-den-pool">Solarstrom für den Pool</a></li><li class=" dropdown-submenu"><a href="/produkte/waermepumpe-photovoltaik">Wärmepumpe &amp; Photovoltaik</a></li><li class="sub dropdown-submenu"><a href="/produkte/waerme-aus-strom">Wärme aus Strom</a><ul class="dropdown-menu"><li class="  dropdown-submenu"><a href="/produkte/waerme-aus-strom/infrarotheizung">Infrarotheizung</a></li><li class="  dropdown-submenu"><a href="/produkte/waerme-aus-strom/waermepumpen">Wärmepumpen</a></li></ul></li><li class=" dropdown-submenu"><a href="/produkte/zubehoer">Zubehör</a></li></ul></li><li class="hasSub dropdown"><a class="d-inline-block" title="Solar installer with all-round service" href="/service"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">service</font></font></a><a href="#" class="dropdown-toggle position-absolute" data-bs-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="true"><span class="caret"></span></a><ul class="dropdown-menu"><li class=" dropdown-submenu"><a href="/service/der-solarstammtisch">Der Solarstammtisch</a></li><li class=" dropdown-submenu"><a href="/service/newsletter">Newsletter</a></li><li class=" dropdown-submenu"><a href="/service/kostenfreie-infoveranstaltung">Kostenfreie Infoveranstaltung</a></li><li class=" dropdown-submenu"><a href="/service/photovoltaik-rechner">Photovoltaik-Rechner</a></li><li class=" dropdown-submenu"><a href="/service/photovoltaikanlage-kaufen">Photovoltaikanlage kaufen</a></li><li class=" dropdown-submenu"><a href="/service/photovoltaikanlage-mieten">Photovoltaikanlage mieten</a></li><li class=" dropdown-submenu"><a href="/service/foerderung-photovoltaik-und-speicher">Förderung Photovoltaik und Speicher</a></li><li class=" dropdown-submenu"><a href="/service/photovoltaik-und-speicher-finanzierung">Photovoltaik- und Speicher-Finanzierung</a></li><li class=" dropdown-submenu"><a href="/service/pvversicherung">PV Versicherung</a></li><li class=" dropdown-submenu"><a href="/service/photovoltaik-leitfaden">Photovoltaik Leitfaden</a></li><li class=" dropdown-submenu"><a href="/service/photovoltaik-faq">Photovoltaik FAQ</a></li><li class=" dropdown-submenu"><a href="/service/photovoltaik-steuer">Photovoltaik Steuer</a></li></ul></li><li class=""><a class="d-inline-block" title="Vacancies and jobs - careers at enerix" href="/karriere"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Career</font></font></a></li><li class="hasSub dropdown"><a class="d-inline-block" title="The photovoltaic specialist chain enerix introduces itself" href="/ueber-enerix"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">about enerix</font></font></a><a href="#" class="dropdown-toggle position-absolute" data-bs-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="true"><span class="caret"></span></a><ul class="dropdown-menu"><li class=" dropdown-submenu"><a href="/ueber-enerix/arbeiten-in-der-photovoltaikbranche">Arbeiten in der Photovoltaikbranche</a></li><li class=" dropdown-submenu"><a href="/ueber-enerix/franchise">Franchise</a></li><li class=" dropdown-submenu"><a href="/ueber-enerix/franchise-oesterreich">Franchise Österreich</a></li><li class=" dropdown-submenu"><a href="/ueber-enerix/stellenangebote/montage-pv">Montagepartner werden</a></li><li class=" dropdown-submenu"><a href="/ueber-enerix/presse">Presse</a></li><li class=" dropdown-submenu"><a href="/ueber-enerix/medienecho">Medienecho</a></li></ul></li><li class=""><a class="d-inline-block" title="blog" href="/blog"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">blog</font></font></a></li><li class="lastItem"><a class="d-inline-block" title="Locations" href="/standorte"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Locations</font></font></a></li></ul></div></div></nav></div><div class="gradient"></div></div></header><div class="topContent text-center"><div id="c12149" class="frame frame-default frame-type-html frame-layout-0"><!-- ProvenExpert Bewertungssiegel --><style type="text/css">body {-ms-overflow-style: scrollbar;} @media(max-width:991px){.ProvenExpert_widget_container {display:none;}}</style><a class="ProvenExpert_widget_container" href="https://www.provenexpert.com/enerix-alternative-energietechnik/?utm_source=Widget&amp;utm_medium=Widget&amp;utm_campaign=Widget" title="Show experiences &amp; reviews about enerix - alternative energy technology" target="_blank" style="text-decoration:none;z-index:9999;position:fixed;float:left;line-height:0;right:0;top:200px;"><img src="https://images.provenexpert.com/74/31/1ea90dfc2e1b4cc32119bc797414/widget_portrait_180_de_0.png" alt="Experiences &amp; reviews about enerix - alternative energy technology" width="180" height="216" style="border:0"></a><!-- ProvenExpert Bewertungssiegel --></div><div id="c60688" class="frame frame-default frame-type-enerix_seoheadertwo frame-layout-0"><div class="seo-header-two container-fluid g-0 position-relative text-left"><div class="row"><div class="col-12 bg-image" style="background-image: url(/fileadmin/_processed_/3/f/csm_photovoltaik_01bcb61f5f.jpg); background-size: cover; background-position: top center;"><div class="textbox float-start w-40 h-100 gradient-bg-headline-normal p-5 pt-4"><p><span style="font-size:3rem"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Tired of rising electricity prices? </font></font></span><br><span style="font-size:2rem"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">enerix helps homeowners get rid of electricity costs. </font><font style="vertical-align: inherit;">Get the good feeling of making your own electricity!</font></font></span></p></div></div></div></div></div><div id="c12615" class="frame frame-default frame-type-html frame-layout-0"><script async="" type="text/javascript" src="//userlike-cdn-widgets.s3-eu-west-1.amazonaws.com/c1a225aa285f9dfcafdae510e092e2408ff9cfcc10a75efda89e4dd335ad5992.js"></script></div></div><!--TYPO3SEARCH_begin--><div class="container-fluid front full nopadding"><div class="maincontent"><div id="c12642" class="frame frame-default frame-type-enerix_simplerow frame-layout-0"><div class="sectionStyle sectionStyle-variantTwo  default noarrow light" id="c12642"><div class="container text-left"><div class="row"><div id="c4401" class="frame frame-default frame-type-header frame-layout-0"><header><h1 class=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            
            
            Photovoltaic &amp; power storage
        </font></font></h1></header></div><div id="c5186" class="frame frame-default frame-type-header frame-layout-0"><header><h2 class=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            
            enerix helps homeowners eliminate their electricity costs with photovoltaics!</font></font></h2></header></div><div id="c17404" class="frame frame-default frame-type-enerix_twocolumn frame-layout-0"><div class="row   default"><div class="col-sm-6   "><div class="col-inner "><div id="c5184" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-left ce-intext"><div class="ce-bodytext"><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Photovoltaic and power storage - With a </font></font><a href="/produkte/photovoltaikanlagen" title="photovoltaic system" target="_self"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">photovoltaic system</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> you turn your roof into a source of energy and you are independent of constantly increasing electricity costs. </font><font style="vertical-align: inherit;">At the same time, you make </font><font style="vertical-align: inherit;">an important contribution to climate protection with your </font></font><a href="/produkte/solaranlage" title="solar system" target="_self"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">solar system .</font></font></a><font style="vertical-align: inherit;"></font></p><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Here you can find out everything about the many advantages of photovoltaics. </font><font style="vertical-align: inherit;">We will show you step by step how big your PV system and your </font></font><a href="/produkte/stromspeicher" title="power storage" target="_self"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">battery storage</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> should be or how you can use solar energy for your electric car or for the heat pump.</font></font></p></div></div></div></div></div><div class="col-sm-6   "><div class="col-inner "><div id="c17613" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/fileadmin/_processed_/6/e/csm_Photovoltaikanlage-auf-Einfamilienhaus_061dc86c64.jpg" alt="Photovoltaic system on family house" title="Photovoltaic system on family house" data-lightbox-caption="" class="lightbox" data-lightbox-width="400" data-lightbox-height="242" rel="lightbox_17613"><img class="image-embed-item" title="Photovoltaic system on family house" alt="Photovoltaic system on family house" src="/fileadmin/_processed_/6/e/csm_Photovoltaikanlage-auf-Einfamilienhaus_d80fdf4baf.jpg" width="400" height="242" loading="lazy"></a></figure></div></div></div></div></div></div></div></div></div></div></div></div></div><div id="c1121" class="frame frame-default frame-type-shortcut frame-layout-0"><div id="c9820" class="frame frame-default frame-type-enerix_simplerow frame-layout-0"><div class="sectionStyle sectionStyle-variantOne  default noarrow light" id="c9820"><div class="container text-left"><div class="row"><div id="c65758" class="frame frame-default frame-type-enerix_twocolumn frame-layout-0"><header><h2 class=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            
            Photovoltaic Guide - Edition 2023</font></font></h2><h3 class=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                Get the ultimate manual for planning your photovoltaic system
            </font></font></h3></header><div class="row   default"><div class="col-sm-4   "><div class="col-inner "><div id="c65759" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-left ce-above"><div class="ce-gallery imageorient-2" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/fileadmin/user_upload/Leitfaden_PV_Speicher/mockup-Leitfaden-2023-PV_Speicher_kl_gratis.png" alt="Photovoltaic guide" title="Photovoltaic guide" data-lightbox-caption="" class="lightbox" data-lightbox-width="600" data-lightbox-height="559" rel="lightbox_65759"><img class="image-embed-item" title="Photovoltaic guide" alt="Photovoltaic guide" src="/fileadmin/user_upload/Leitfaden_PV_Speicher/mockup-Leitfaden-2023-PV_Speicher_kl_gratis.png" width="600" height="559" loading="lazy"></a></figure></div></div></div></div></div></div></div><div class="col-sm-8   "><div class="col-inner "><div id="c65761" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-left ce-above"><div class="ce-bodytext"><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">With more than 100,000 copies sent, the </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">photovoltaic guide</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> is the most frequently used guide when planning private photovoltaic systems. </font><font style="vertical-align: inherit;">It contains the knowledge from more than 20 years of experience in the industry and from more than 35,000 installed solar systems. </font><font style="vertical-align: inherit;">The guide takes you through the planning of your systems in 10 steps.&nbsp;</font></font></p><ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The guide will help you plan your system step by step</font></font></li><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">You </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">save time and money</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> when researching your solar system</font></font></li><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">You will receive important tips, calculation examples and checklists</font></font></li><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">You increase your competence and avoid mistakes in planning</font></font></li><li><font style="vertical-align: inherit;"></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Rated " VERY GOOD</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> " </font><font style="vertical-align: inherit;">over 10,000 times</font></font></li><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">You will receive the guide in the digital edition completely&nbsp; </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">free of charge</font></font></strong></li></ul></div></div></div><div id="c65760" class="frame frame-default frame-type-enerix_button frame-layout-0"><div class="buttonwrap"><a role="button" class="btn btn-danger btn-lg btn-block  " title="Get your free copy here" href="/service/photovoltaik-leitfaden"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                        Get your free copy here
                        
                    </font></font></a></div></div></div></div></div></div></div></div></div></div></div><div id="c14955" class="frame frame-default frame-type-enerix_simplerow frame-layout-0"><div class="sectionStyle sectionStyle-normal  default noarrow light" id="c14955"><div class="container text-left"><div class="row"><div id="c11661" class="frame frame-default frame-type-header frame-layout-0"><header><h2 class=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            
            3 building blocks for your solar self-sufficiency</font></font></h2></header></div><div id="c4514" class="frame frame-default frame-type-enerix_threecolumn frame-layout-0"><div class="row    "><div class="col-sm-4   "><div id="c22486" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            
            Photovoltaic system - simply make solar power yourself</font></font></h3></header><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><img class="image-embed-item" title="Photovoltaic system on family house" alt="Photovoltaic system on family house" src="/fileadmin/_processed_/d/f/csm_Photovoltaikanlage_f%C3%BCr_Wohnhaus_kaufen__01_0cbfd777a4.jpg" width="448" height="252" loading="lazy"></figure></div></div></div></div></div><div class="ce-bodytext"><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">What if you could simply make your own electricity and much cheaper than from the electricity company? </font><font style="vertical-align: inherit;">With a photovoltaic system on your roof, you produce a lot of electricity that you can put to good use. </font><font style="vertical-align: inherit;">You can find out how a PV system is structured here.</font></font></p></div></div></div><div id="c4517" class="frame frame-default frame-type-enerix_button frame-layout-0"><div class="buttonwrap"><a role="button" class="btn btn-default  btn-block  " title="Modules, inverters and roof rack" href="/produkte/photovoltaikanlagen"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                        Modules, inverters and roof rack
                        
                    </font></font></a></div></div></div><div class="col-sm-4   "><div id="c22487" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class=""><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
            
            Power storage - solar power at any time of the day or night</font></font></h3></header><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><img class="image-embed-item" title="Funktionsweise Stromspeicher" alt="Funktionsweise Stromspeicher" src="/fileadmin/user_upload/produkte/Speicher/Grafik_Stromspeicher.png" width="600" height="337" loading="lazy"></figure></div></div></div></div></div><div class="ce-bodytext"><p>Stromspeicher machen PV-Anlagen erst richtig effektiv denn damit kannst du deinen Solarstrom zu jeder Tages- und Nachtzeit nutzen. Stromspeicher erhöhen deine Autarkie auf bis zu 80 Prozent. Und machen dich noch unabhängiger. So funktioniert ein Stromspeicher.</p></div></div></div><div id="c4520" class="frame frame-default frame-type-enerix_button frame-layout-0"><div class="buttonwrap"><a role="button" class="btn btn-default  btn-block  " title="Weiter zu den Stromspeichern" href="/produkte/stromspeicher">
                        Weiter zu den Stromspeichern
                        
                    </a></div></div></div><div class="col-sm-4   "><div id="c22488" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class="">
            
            Stromcloud - Ein Stromsparkonto für deinen überschüssigen Strom</h3></header><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><img class="image-embed-item" title="Photovoltaik Stromcloud" alt="Photovoltaik Stromcloud" src="/fileadmin/_processed_/e/8/csm_Grafik_Stromcloud_7d0c1487d7.jpg" width="595" height="331" loading="lazy"></figure></div></div></div></div></div><div class="ce-bodytext"><p>Die Stromcloud ist eine geniale Idee für Stunden in denen die Sonne nicht scheint und dein Speicher leer ist. Die Cloud ist ein Stromsparkonto, auf dem du deinen Stromüberschuss einzahlst und bei Bedarf wieder abrufst. Wie die Cloud funktioniert erfährst du hier.</p></div></div></div><div id="c4521" class="frame frame-default frame-type-enerix_button frame-layout-0"><div class="buttonwrap"><a role="button" class="btn btn-default  btn-block  " title="Weiter zur Stromcloud" href="/produkte/stromcloud">
                        Weiter zur Stromcloud
                        
                    </a></div></div></div></div></div></div></div></div></div><div id="c2006" class="frame frame-default frame-type-enerix_simplerow frame-layout-0"><div class="sectionStyle sectionStyle-variantTwo  default noarrow light" id="c2006"><div class="container text-left"><div class="row"><div id="c23630" class="frame frame-default frame-type-header frame-layout-0"><header><h2 class="">
            
            Wichtige Informationen rund ums Thema Photovoltaik, Stromspeicher &amp; Co.</h2></header></div><div id="c2007" class="frame frame-default frame-type-enerix_fourcolumn frame-layout-0"><div class="row  default "><div class="col-md-3 col-sm-6   "><div id="c2008" class="frame frame-default frame-type-enerix_teaser frame-layout-0"><div class="teaser article_box default "><a title="Der Solarstammtisch - Video-Podcast" href="/service/der-solarstammtisch"><div class="photo_mask"><img class="img-fluid" title="Der Solarstammtisch - Video-Podcast" alt="Der Solarstammtisch - Video-Podcast" src="/fileadmin/_processed_/1/f/csm_solarstammtisch_2186a28bf7.jpg" width="540" height="405"><div class="mask"></div><span class="button_image more"><span class="fa fa-link"></span></span></div></a><div class="desc_wrapper" style="height: 340.344px;"><h4 class="title">Der Solarstammtisch - Video-Podcast</h4><div class="desc"><p>Bilder sagen mehr als tausend Worte und Filme können komplexe Themen einfach besser erklären. In den kurzen Videos sprechen wir über alle Themen rund um Photovoltaik, die solare Energieversorgung, zeigen dir, welche Komponenten wichtig sind und stellen Produkte vor.</p></div></div><a class="btn btn-default btn-lg" title="Der Solarstammtisch - Video-Podcast" href="/service/der-solarstammtisch">Zum Solarstammtisch</a></div></div></div><div class="col-md-3 col-sm-6   "><div id="c12141" class="frame frame-default frame-type-enerix_teaser frame-layout-0"><div class="teaser article_box default "><a title="Photovoltaik Förderung" href="/service/foerderung-photovoltaik-und-speicher"><div class="photo_mask"><img class="img-fluid" title="Photovoltaik Förderung" alt="Photovoltaik Förderung" src="/fileadmin/_processed_/e/1/csm_T-finanzierung_d7daf5d3c8.jpg" width="540" height="405"><div class="mask"></div><span class="button_image more"><span class="fa fa-link"></span></span></div></a><div class="desc_wrapper" style="height: 340.344px;"><h4 class="title">Photovoltaik Förderung</h4><div class="desc"><p>Die Investitionen in Photovoltaik und Stromspeicher werden in Deutschland über verschiedene Landes- oder Bundesgesetze gefördert. Aber nicht in allen Fällen ist die Nutzung einer Förderung sinnvoll, da teilweise gewisse Verpflichtungen mit der Förderung für den Betreiber verknüpft werden.</p></div></div><a class="btn btn-default btn-lg" title="Photovoltaik Förderung" href="/service/foerderung-photovoltaik-und-speicher">Mehr zu den Förderungen</a></div></div></div><div class="col-md-3 col-sm-6   "><div id="c2010" class="frame frame-default frame-type-enerix_teaser frame-layout-0"><div class="teaser article_box default "><a title="Photovoltaik Kredit" href="/service/photovoltaik-und-speicher-finanzierung"><div class="photo_mask"><img class="img-fluid" title="Photovoltaik Kredit" alt="Photovoltaik Kredit" src="/fileadmin/_processed_/7/b/csm_T-enerix-solarkredit_2bbf3aedb1.jpg" width="540" height="400"><div class="mask"></div><span class="button_image more"><span class="fa fa-link"></span></span></div></a><div class="desc_wrapper" style="height: 340.344px;"><h4 class="title">Photovoltaik Kredit</h4><div class="desc"><p>Hier erhältst du die wichtigsten Infos zu den Finanzierungsmöglichkeiten deines Photovoltaik- und Solarstromspeichersystems. Den Antrag kannst du hier ganz einfach online stellen.</p></div></div><a class="btn btn-default btn-lg" title="Photovoltaik Kredit" href="/service/photovoltaik-und-speicher-finanzierung">Zum Solarkredit</a></div></div></div><div class="col-md-3 col-sm-6   "><div id="c2012" class="frame frame-default frame-type-enerix_teaser frame-layout-0"><div class="teaser article_box default "><a title="Solarparty" href="/solarparty"><div class="photo_mask"><img class="img-fluid" title="Solarparty" alt="Solarparty" src="/fileadmin/_processed_/1/6/csm_Solarparty_375de950cd.jpg" width="540" height="405"><div class="mask"></div><span class="button_image more"><span class="fa fa-link"></span></span></div></a><div class="desc_wrapper" style="height: 340.344px;"><h4 class="title">Solarparty</h4><div class="desc"><p>Du bist enerix-Kunde und hast deine Stromversorgung selbst in die Hand genommen? Möchtest du deine Freunde, Nachbarn oder Bekannte motivieren das Gleiche zu tun? Dann lade sie doch mal zu dir ein.</p></div></div><a class="btn btn-default btn-lg" title="Solarparty" href="/solarparty">Solarparty veranstalten</a></div></div></div></div></div></div></div></div></div><div id="c4992" class="frame frame-default frame-type-enerix_simplerow frame-layout-0"><div class="sectionStyle sectionStyle-normal  default arrow light" id="c4992"><div class="container text-left"><div class="row"><div id="c5000" class="frame frame-default frame-type-header frame-layout-0"><header><h2 class="">
            
            Nutze die Vorteile der Photovoltaik und mach dein Dach zur Energiequelle</h2></header></div><div id="c4993" class="frame frame-default frame-type-enerix_threecolumn frame-layout-0"><div class="row    "><div class="col-sm-4   "><div id="c4997" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class="">
            
            1. Photovoltaik ist die sauberste und umweltfreundlichste Art der Stromproduktion</h3></header><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>Solarstrom wird ohne Verbrennung oder sonstige umweltschädliche Einflüsse hergestellt. Die <a href="/produkte/solaranlage" title="Solaranlage" target="_self" class="internal-link"><strong>Solaranlage</strong></a> auf dem eigenen Dach verbraucht keine zusätzlichen Flächen oder benötigt Stromtrassen.</p></div></div></div><div id="c4996" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class="">
            
            4. Photovoltaik steigert den Wert deiner Immobilie</h3></header><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>Eine dezentrale Energieversorgung mit Photovoltaik spielt eine immer wichtigere Rolle, auch beim Verkauf oder bei der Vermietung der Immobilie. Vergleiche zeigen, dass Immobilien mit einer Photovoltaikanlage bei Käufern oder Mietern wesentlich attraktiver sind.</p></div></div></div></div><div class="col-sm-4   "><div id="c4994" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class="">
            
            2. Photovoltaikanlagen haben eine extrem hohe Lebensdauer</h3></header><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>Photovoltaikmodule sind einfach unkaputtbar, ihre Lebensdauer ist weit über 20 Jahre. Das ist möglich aufgrund fehlender mechanischer Belastungen und durch sehr hohe Qualitätsstandards. Das Ganze wird durch Garantien der Hersteller abgesichert.</p></div></div></div><div id="c4999" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class="">
            
            5. Kosten–Nutzen-Faktor</h3></header><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>Es gibt nur wenige Investitionen, die einen solchen Kosten-Nutzen-Faktor haben wie die Photovoltaik. In der Regel refinanziert sich ein Photovoltaik-System durch die Energiekosteneinsparung. Und mit den günstigen <strong><a href="/service/photovoltaik-und-speicher-finanzierung" title="Hier bekommst Du weitere Details zu den Finanzierungsmöglichkeiten" target="_self">Finanzierungsmöglichkeiten</a></strong>muss man kein eigenes Geld in die Hand nehmen.</p></div></div></div></div><div class="col-sm-4   "><div id="c4995" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class="">
            
            3. Photovoltaikanlagen sind einfach in der Handhabung</h3></header><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>PV-Anlagen und Stromspeicher sind einfach in ihrer Handhabung. Sie schalten sich automatisch ein und aus und müssen nur alle paar Jahre gewartet werden. Auch eine Reinigung ist i.d.R. nicht notwendig, da sich die Photovoltaikmodule durch Regen und Schnee selbst reinigen.</p></div></div></div><div id="c4998" class="frame frame-default frame-type-textmedia frame-layout-0"><header><h3 class="">
            
            6. Solarstromanlagen besitzen einen hohen Wirkungsgrad</h3></header><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>Das Dach eines Einfamilienhauses reicht aus um den Jahresstrombedarf einer vierköpfigen Familie zu produzieren. Im Sommer mehr als im Winter und auch nur am Tag, aber es gibt ja Stromspeicher und die Stromcloud.</p></div></div></div></div></div></div></div></div></div></div><div id="c50902" class="frame frame-default frame-type-enerix_simplerow frame-layout-0"><div class="sectionStyle sectionStyle-variantTwo  default noarrow light" id="c50902"><div class="container text-center"><div class="row"><div id="c50912" class="frame frame-default frame-type-header frame-layout-0"><header><h2 class="">
            
            Photovoltaikreferenzen - Das sagen Kunden über uns!</h2></header></div><div id="c50913" class="frame frame-default frame-type-div frame-layout-0"><hr class="ce-div"></div><div id="c50903" class="frame frame-default frame-type-enerix_threecolumn frame-layout-0"><div class="row    "><div class="col-sm-4   "><div id="c50904" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>"Ich bin hoch zufrieden mit meiner PV Anlage. Von der Beratung über die Installation bis zur Übergabe lief alles einwandfrei. Ich kann enerix nur empfehlen. Speziellen Dank an Herrn Choreny für den schnellen und kompetenten Support bei einer Störung am Speicher."<br><img alt="Sterne-Bewertung" src="/fileadmin/_processed_/e/f/csm_Photovoltaik_Kundenbewertung_5_Sterne_84290303a8.png" width="298" height="65" loading="lazy"><br> Ganser S. für enerix Minden</p></div></div></div></div><div class="col-sm-4   "><div id="c50905" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>"Besonders zufrieden war ich mit der sehr guten Beratung, Unterstützung während der Installation und auch danach war immer jemand erreichbar. Bei Förderanträgen wurden wir auch sehr gut unterstützt!<br> Vielen Dank an das gesamte Team!"<br><img alt="Sterne-Bewertung" src="/fileadmin/_processed_/e/f/csm_Photovoltaik_Kundenbewertung_5_Sterne_84290303a8.png" width="298" height="65" loading="lazy"><br> Kolbeck Alois für enerix-Regenburg<br> &nbsp;</p></div></div></div></div><div class="col-sm-4   "><div id="c50906" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>"Kompetente Beratung durch Herrn Richter und Herrn Balzer in Burglengenfeld. Sofortige Hilfe bei Fragen. Montage schnell, sauber unter präziser Einhaltung sämtlicher Termine. Handwerker alle motiviert und freundlich.<br> Bestnote!"<br><img alt="Sterne-Bewertung" src="/fileadmin/_processed_/e/f/csm_Photovoltaik_Kundenbewertung_5_Sterne_84290303a8.png" width="298" height="65" loading="lazy"><br> Heribert Krotter für enerix-Schwandorf</p></div></div></div></div></div></div><div id="c50911" class="frame frame-default frame-type-div frame-layout-0"><hr class="ce-div"></div><div id="c50909" class="frame frame-default frame-type-html frame-layout-0"><!-- ProvenExpert Bewertungssiegel --><div id="pewl" class="pewl"><div class="pew-header pew-a pew-f pew-c pew-s pew-not-b pew-not-e"><a class="pew-go" href="https://www.provenexpert.com/enerix-alternative-energietechnik/?utm_source=Widget&amp;utm_medium=Widget&amp;utm_campaign=Widget" target="_blank" title="Kundenbewertungen &amp; Erfahrungen zu enerix - Alternative Energietechnik. Mehr Infos anzeigen.">Mehr Infos<span class="pew-moreInfo"></span></a><img src="https://www.provenexpert.com/images/widget/provenexpert_logo_black.png" width="173" height="24" alt="ProvenExpert"><span class="pew-title-label">Kundenbewertungen</span> </div> <div class="pew-content pew-a pew-f pew-c pew-s pew-not-b pew-not-e pew-v2"><div class="pew-left"><div><img src="https://images.provenexpert.com/74/31/1ea90dfc2e1b4cc32119bc797414/enerix-alternative-energietechnik_medium_1539661810.jpg" alt="enerix - Alternative Energietechnik"></div></div><div class="pew-middle"><div><div class="pew-left pew-centerText"><span></span><span>20.216 Bewertungen</span></div><div class="pew-middle"><div><div class="" id="rating_4" style="left: 0%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_5" style="left: -110%;"><p class="pew-1">4.80 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_6" style="left: -110%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_7" style="left: -110%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_8" style="left: -110%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_9" style="left: -110%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_10" style="left: -110%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_1" style="left: -110%;"><p class="pew-1">4.75 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_2" style="left: -110%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div><div class="pew-hidden" id="rating_3" style="left: -110%;"><p class="pew-1">5.00 von 5</p><p class="pew-2"><span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span><span class="pew-star pew-gold"></span></span></p><p class="pew-3">SEHR GUT</p></div></div></div><div class="pew-right pew-centerText"><div><div><span></span><span>Empfehlung</span></div></div></div></div></div><div class="pew-right"><div><div><div class="" data-rating="4" style="left: 0%;"><span class="pew-author">14.05.2023</span><span class="pew-feedback">Empfehlung! Von der Beratung, über die Montage bis hin zur Inbetriebnahme hat aus unserer Sicht alles Top geklappt und wir können und werden Sie gerne weiterempfehlen</span></div><div class="pew-hidden" data-rating="5" style="left: -110%;"><span class="pew-author">13.05.2023</span><span class="pew-feedback">Empfehlung! Ich war von der Planung bis zum Ende der Durchführung sehr zufrieden mit dem Service.</span></div><div class="pew-hidden" data-rating="6" style="left: -110%;"><span class="pew-author">12.05.2023</span><span class="pew-feedback">Empfehlung! 5 von 5 Sternen.</span></div><div class="pew-hidden" data-rating="7" style="left: -110%;"><span class="pew-author">12.05.2023</span><span class="pew-feedback">Empfehlung! 5 von 5 Sternen.</span></div><div class="pew-hidden" data-rating="8" style="left: -110%;"><span class="pew-author">12.05.2023</span><span class="pew-feedback">Empfehlung! Die Beratung war sehr gut, es wurden trotz schwieriger Bedingungen kreative Lösungen gefunden. Auch die Montage der einzelnen Komponenten war sehr professionell. Lediglich die sehr lange Lieferzeit des RCT Wechselrichters hat den sehr guten Gesamteindruck ein wenig getrübt.</span></div><div class="pew-hidden" data-rating="9" style="left: -110%;"><span class="pew-author">12.05.2023</span><span class="pew-feedback">Empfehlung! Alle Mitarbeiter sind sehr freundlich, kompetent und zuverlässig.</span></div><div class="pew-hidden" data-rating="10" style="left: -110%;"><span class="pew-author">12.05.2023</span><span class="pew-feedback">Empfehlung! 5 von 5 Sternen.</span></div><div class="pew-hidden" data-rating="1" style="left: -110%;"><span class="pew-author">15.05.2023</span><span class="pew-feedback">Empfehlung! 5 von 5 Sternen.</span></div><div class="pew-hidden" data-rating="2" style="left: -110%;"><span class="pew-author">15.05.2023</span><span class="pew-feedback">Empfehlung! Vom Erstkontakt über die Beratung, bis zur Umsetzung des Projektes eine hervorragende Betreuung durch Herrn Mike Zöller. Sämtliche Arbeiten wurden termingerecht, sachgerecht und sauber durchgeführt. Note 1 + für den Berater und für das gesamte Team.</span></div><div class="pew-hidden" data-rating="3" style="left: -110%;"><span class="pew-author">14.05.2023</span><span class="pew-feedback">Empfehlung! 5 von 5 Sternen.</span></div></div></div></div></div> <div class="pew-footer pew-a pew-f pew-c pew-s pew-not-b pew-not-e"><div style="float:right;"><a style="float:left;" class="pew-go" href="https://www.provenexpert.com/enerix-alternative-energietechnik/?utm_source=Widget&amp;utm_medium=Widget&amp;utm_campaign=Widget" target="_blank" title="Kundenbewertungen &amp; Erfahrungen zu enerix - Alternative Energietechnik. Mehr Infos anzeigen.">Mehr Infos<span class="pew-moreInfo"></span></a></div><div><span class="pew-bold">Top-Kompetenzen:</span><span class="pew-check"></span>Kundenzufriedenheit<span class="pew-check"></span>Kundentreue<span class="pew-check"></span>Auftragserfolg</div></div></div><script type="text/javascript" src="https://www.provenexpert.com/widget/landing_enerix-alternative-energietechnik.js?feedback=1&amp;avatar=1&amp;competence=1&amp;style=white"></script><link rel="stylesheet" type="text/css" href="https://www.provenexpert.com/css/widget_landing.css" media="screen,print"><!-- ProvenExpert Bewertungssiegel Ende --></div></div></div></div></div><div id="c1990" class="frame frame-default frame-type-enerix_simplerow frame-layout-0"><div class="sectionStyle sectionStyle-variantOne  default arrow light" id="c1990"><div class="container text-center"><div class="row"><div id="c1995" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-center ce-above"><div class="ce-bodytext"><p class="h2">In drei Schritten zum Photovoltaik- und Stromspeichersystem </p></div></div></div><div id="c1991" class="frame frame-default frame-type-enerix_threecolumn frame-layout-0"><div class="row    "><div class="col-sm-4   "><div id="c1992" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><img class="image-embed-item" title="Photovoltaikfachbetrieb kontaktieren" alt="Photovoltaikfachbetrieb kontaktieren" src="/fileadmin/_processed_/d/a/csm_icon-Phone_bd9ccfa80c.png" width="200" height="200" loading="lazy"></figure></div></div></div></div></div><div class="ce-bodytext"><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">1. Contact</font></font></p><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">You contact the enerix company in your area and provide us with initial information about your energy requirements and your wishes.&nbsp;</font></font></p></div></div></div></div><div class="col-sm-4   "><div id="c1993" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><img class="image-embed-item" title="Photovoltaikanlage kalkulieren" alt="Photovoltaikanlage kalkulieren" src="/fileadmin/_processed_/9/a/csm_icon-Angebot_3e71f5a945.png" width="200" height="200" loading="lazy"></figure></div></div></div></div></div><div class="ce-bodytext"><p class="h3"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2. Calculate</font></font></p><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">We plan your system together, calculate your annual savings and create a turnkey offer for you.</font></font></p></div></div></div></div><div class="col-sm-4   "><div id="c1994" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><img class="image-embed-item" title="Photovoltaik und Stromspeicher installieren" alt="Photovoltaik und Stromspeicher installieren" src="/fileadmin/_processed_/b/d/csm_icon-Installation_836f76a93b.png" width="200" height="200" loading="lazy"></figure></div></div></div></div></div><div class="ce-bodytext"><p class="h3"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3. Install</font></font></p><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">You commission enerix and we take care of all the details for the assembly and installation of your photovoltaic system and your power storage.</font></font></p></div></div></div></div></div></div><div id="c2013" class="frame frame-default frame-type-enerix_button frame-layout-0"><div class="buttonwrap"><a href="/kontakt" title="Beratungstermin vereinbaren" target="43" class="btn btn-danger btn-lg" role="button"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                        arrange an appointment for consultation
                        
                            
                                
                                    
                                
                                    
                                
                            
                        
                    </font></font></a></div></div></div></div></div></div><div id="c20109" class="frame frame-default frame-type-enerix_twocolumn frame-layout-0"><div class="row   default"><div class="col-sm-6   "><div class="col-inner "><div id="c20116" class="frame frame-default frame-type-enerix_sixcolumn frame-layout-0"><div class="row   "><div class="col-sm-2   "></div><div class="col-sm-2   "><div id="c20100" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/photovoltaikanlagen/solaredge" title="Solaredge Wechselrichter" target="_self"><img class="image-embed-item" title="Solaredge Wechselrichter" alt="Solaredge Wechselrichter" src="/fileadmin/user_upload/Logos_Lieferanten/SolarEdge_logo_web_16x9_01.jpg" width="800" height="450" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20111" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/solarstromspeicher/e3dc" title="E3dc Stromspeicher" target="_self"><img class="image-embed-item" title="E3dc Stromspeicher" alt="E3dc Stromspeicher" src="/fileadmin/user_upload/Bilder_Lieferanten/e3dc_Stromspeicher/e3dc_logo.jpg" width="455" height="256" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20112" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/photovoltaikanlagen/heckert" title="Heckert Photovoltaikmodule" target="_self"><img class="image-embed-item" title="Heckert Photovoltaikmodule" alt="Heckert Photovoltaikmodule" src="/fileadmin/_processed_/9/c/csm_heckert-solar-logo_web_16x9_02_0d08b87577.jpg" width="727" height="409" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20115" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/solarstromspeicher/sonnenbatterie" title="sonnen Stromspeicher" target="_self"><img class="image-embed-item" title="sonnen Stromspeicher" alt="sonnen Stromspeicher" src="/fileadmin/_processed_/a/a/csm_sonnen_logo_horizontal_web_16x9_01_7333b3f905.jpg" width="769" height="432" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20110" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/photovoltaikanlagen/fronius" title="Fronius Wechselrichter" target="_self"><img class="image-embed-item" title="Fronius Wechselrichter" alt="Fronius Wechselrichter" src="/fileadmin/_processed_/4/2/csm_Fronius-Logo-DE_web_16x9_01_6bdf4e41b8.jpg" width="614" height="345" loading="lazy"></a></figure></div></div></div></div></div></div></div></div></div></div><div class="col-sm-6   "><div class="col-inner "><div id="c20101" class="frame frame-default frame-type-enerix_sixcolumn frame-layout-0"><div class="row   "><div class="col-sm-2   "><div id="c20113" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/solarstromspeicher/senec" title="senec Stromspeicher" target="_self"><img class="image-embed-item" title="senec Stromspeicher" alt="senec Stromspeicher" src="/fileadmin/_processed_/d/7/csm_SENEC.IES_Logo_web_16x9_01_2898b0b0fd.jpg" width="835" height="464" loading="lazy"></a></figure></div></div></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20099" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/photovoltaikanlagen/solarwatt" title="Solarwatt Photovoltaikmodule" target="_self"><img class="image-embed-item" title="Solarwatt Photovoltaikmodule" alt="Solarwatt Photovoltaikmodule" src="/fileadmin/user_upload/Bilder_Lieferanten/Bilder_Solarwatt/solarwatt_Logo_16_9.jpg" width="1878" height="1056" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20097" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/photovoltaikanlagen/q-cells-module" title="Qcells Photovoltaikmodule" target="_self"><img class="image-embed-item" title="Qcells Photovoltaikmodule" alt="Qcells Photovoltaikmodule" src="/fileadmin/user_upload/Qcells.jpg" width="266" height="150" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20095" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/photovoltaikanlagen/aleo" title="aleo Photovoltaikmodule" target="_self"><img class="image-embed-item" title="aleo Photovoltaikmodule" alt="aleo Photovoltaikmodule" src="/fileadmin/_processed_/5/3/csm_aleo_logo_grey_web_01_b603715291.jpg" width="567" height="319" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "><div id="c20098" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-gallery imageorient-17" data-ce-columns="1" data-ce-images="1"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="/produkte/solarstromspeicher/rct-power" title="RCT Power Stromspeicher" target="_self"><img class="image-embed-item" title="RCT Power Stromspeicher" alt="RCT Power Stromspeicher" src="/fileadmin/user_upload/Bilder_Lieferanten/RCT_Power/RCT_POWER-LOGO.jpg" width="455" height="256" loading="lazy"></a></figure></div></div></div></div></div></div><div class="col-sm-2   "></div></div></div></div></div></div></div></div></div><!--TYPO3SEARCH_end--><footer id="footer" data-file="Footer"><div class="container"><script type="text/javascript" src="https://klicktipp.s3.amazonaws.com/userimages/112764/forms/172537/40tmz2m1tz8z57f3.js"></script>
  <style>

    @keyframes slide-out {
      0%   {
        bottom: -658px;
      }
      100% {
        bottom: 0px;
      }
    }

    @-moz-keyframes slide-out-ff {
      0% {
        bottom: -658px;
      }
      100% {
        bottom: 25px;
      }
    }

    @keyframes slide-out-left {
      0%   {
        left: -350px;
      }
      100% {
        left: 0px;
      }
    }

    @keyframes slide-out-right {
      0%   {
        right: -350px;
      }
      100% {
        right: 0px;
      }
    }

    @keyframes slide-in {
      0%   {
        bottom: 0px;
      }
      100% {
        bottom: -658px;
      }
    }

    @keyframes slide-in-left {
      0%   {
        left: 0px;
      }
      100% {
        left: -350px;
      }
    }

    @keyframes slide-in-right {
      0%   {
        right: 0px;
      }
      100% {
        right: -350px;
      }
    }

    @keyframes hide-button {
      0%   {
        opacity: 1;
        -webkit-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
        -moz-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
        box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
      }
      100% {
        opacity: 0;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;
      }
    }

    @keyframes show-button {
      0%   {
        opacity: 0;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;
      }
      100% {
        opacity: 1;
        -webkit-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
        -moz-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
        box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
      }
    }

    @keyframes border-out {
      0%   {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-top-right-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-topright: 0px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
      }
      50%   {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-top-right-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-topright: 0px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
      }
      100% {
        -webkit-border-top-left-radius: 8px;
        -webkit-border-top-right-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-topright: 8px;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
      }
    }

    @keyframes border-out-left {
      0%   {
        -webkit-border-top-right-radius: 0px;
        -webkit-border-bottom-right-radius: 0px;
        -moz-border-radius-topright: 0px;
        -moz-border-radius-bottomright: 0px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
      }
      50%   {
        -webkit-border-top-right-radius: 0px;
        -webkit-border-bottom-right-radius: 0px;
        -moz-border-radius-topright: 0px;
        -moz-border-radius-bottomright: 0px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
      }
      100% {
        -webkit-border-top-right-radius: 8px;
        -webkit-border-bottom-right-radius: 8px;
        -moz-border-radius-topright: 8px;
        -moz-border-radius-bottomright: 8px;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
      }
    }

    @keyframes border-out-right {
      0%   {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-bottom-left-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-bottomleft: 0px;
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
      }
      50%   {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-bottom-left-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-bottomleft: 0px;
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
      }
      100% {
        -webkit-border-top-left-radius: 8px;
        -webkit-border-bottom-left-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-bottomleft: 8px;
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
      }
    }

    @keyframes border-in {
      0%   {
        -webkit-border-top-left-radius: 8px;
        -webkit-border-top-right-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-topright: 8px;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
      }
      50% {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-top-right-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-topright: 0px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
      }
      100% {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-top-right-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-topright: 0px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
      }
    }

    @keyframes border-in-left {
      0%   {
        -webkit-border-top-right-radius: 8px;
        -webkit-border-bottom-right-radius: 8px;
        -moz-border-radius-topright: 8px;
        -moz-border-radius-bottomright: 8px;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
      }
      50%   {
        -webkit-border-top-right-radius: 0px;
        -webkit-border-bottom-right-radius: 0px;
        -moz-border-radius-topright: 0px;
        -moz-border-radius-bottomright: 0px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
      }
      100% {
        -webkit-border-top-right-radius: 0px;
        -webkit-border-bottom-right-radius: 0px;
        -moz-border-radius-topright: 0px;
        -moz-border-radius-bottomright: 0px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
      }
    }

    @keyframes border-in-right {
      0%   {
        -webkit-border-top-left-radius: 8px;
        -webkit-border-bottom-left-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-bottomleft: 8px;
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
      }
      50%   {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-bottom-left-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-bottomleft: 0px;
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
      }
      100% {
        -webkit-border-top-left-radius: 0px;
        -webkit-border-bottom-left-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-bottomleft: 0px;
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
      }
    }

    @-moz-document url-prefix() {
      iframe.ktv2 {
        height: calc(607px + 25px)!important;
        padding-top: 25px!important;
      }
    }

    .ktv2-widget {
      position:fixed;
      width: 350px;
      z-index: 9999;
    }

    .ktv2-widget,
    .ktv2-widget * {
      font-family: \”proxima-nova\”, "Helvetica Neue", Helvetica, Arial, sans-serif;
      font-size: 14px;
      line-height: 20px;
    }

    .ktv2-widget, .ktv2-widget::before, .ktv2-widget::after,
    .ktv2-widget *, .ktv2-widget *::before, .ktv2-widget *::after {
      box-sizing: border-box;
    }

    .ktv2-widget .ktv2-widget-body {
      position:relative;
      width:350px;
      padding: 5px;
      text-align: center;
    }

    .ktv2-widget.ktv2-open-form .ktv2-widget-body {
      -webkit-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
        -moz-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
        box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
    }

    .ktv2-widget .ktv2-widget-body,
    .ktv2-widget.ktv2-open-form.ktv2-close-form {
      -webkit-box-shadow: none;
      -moz-box-shadow: none;
      box-shadow: none;
    }

    .ktv2-widget.widget-bottom-left {
      left: 30px;
      bottom: -658px;
    }

    .ktv2-widget.widget-bottom-right {
      right: 30px;
      bottom: -658px;
    }

    @-moz-document url-prefix() {
      .ktv2-widget.widget-bottom-left, .ktv2-widget.widget-bottom-right {
        margin-bottom: -25px;
      }
    }

    .ktv2-widget.widget-bottom-left.ktv2-open-form,
    .ktv2-widget.widget-bottom-right.ktv2-open-form {
      animation-name: slide-out;
      animation-duration: 1s;
      bottom: 0;
    }
    @-moz-document url-prefix() {
     .ktv2-widget.widget-bottom-left.ktv2-open-form,
     .ktv2-widget.widget-bottom-right.ktv2-open-form {
        animation-name: slide-out-ff;
        bottom: 25px;
      }
    }

    .ktv2-widget.widget-bottom-left.ktv2-open-form.ktv2-close-form .ktv2-widget-body,
    .ktv2-widget.widget-bottom-right.ktv2-open-form.ktv2-close-form .ktv2-widget-body {
      animation-name: border-in;
      animation-duration: 1s;
      -webkit-border-top-left-radius: 0px;
      -webkit-border-top-right-radius: 0px;
      -moz-border-radius-topleft: 0px;
      -moz-border-radius-topright: 0px;
      border-top-left-radius: 0px;
      border-top-right-radius: 0px;
      -webkit-box-shadow: none;
      -moz-box-shadow: none;
      box-shadow: none;
    }

    @media (min-width: 381px) {

      .ktv2-widget.widget-left {
        left: -350px;
        top: 50%;
        margin-top: -329px;
      }

      .ktv2-widget.widget-right {
        right: -350px;
        top: 50%;
        margin-top: -329px;
      }

      .ktv2-widget.widget-left.ktv2-open-form {
        animation-name: slide-out-left;
        animation-duration: 1s;
        left: 0;
      }

      .ktv2-widget.widget-right.ktv2-open-form {
        animation-name: slide-out-right;
        animation-duration: 1s;
        right: 0;
      }

      .ktv2-widget.widget-left.ktv2-open-form .ktv2-widget-body {
        animation-name: border-out-left;
        animation-duration: 1s;
        -webkit-border-top-right-radius: 8px;
        -webkit-border-bottom-right-radius: 8px;
        -moz-border-radius-topright: 8px;
        -moz-border-radius-bottomright: 8px;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
      }

      .ktv2-widget.widget-right.ktv2-open-form .ktv2-widget-body {
        animation-name: border-out-right;
        animation-duration: 1s;
        -webkit-border-top-left-radius: 8px;
        -webkit-border-bottom-left-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-bottomleft: 8px;
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
      }

      .ktv2-widget.widget-left.ktv2-open-form.ktv2-close-form {
        animation-name: slide-in-left;
        animation-duration: 1s;
        left: -350px;
      }

      .ktv2-widget.widget-right.ktv2-open-form.ktv2-close-form {
        animation-name: slide-in-right;
        animation-duration: 1s;
        right: -350px;
      }

      .ktv2-widget.widget-left.ktv2-open-form.ktv2-close-form .ktv2-widget-body {
        animation-name: border-in-left;
        animation-duration: 1s;
        -webkit-border-top-right-radius: 0px;
        -webkit-border-bottom-right-radius: 0px;
        -moz-border-radius-topright: 0px;
        -moz-border-radius-bottomright: 0px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;
      }

      .ktv2-widget.widget-right.ktv2-open-form.ktv2-close-form .ktv2-widget-body {
        animation-name: border-in-right;
        animation-duration: 1s;
        -webkit-border-top-left-radius: 0px;
        -webkit-border-bottom-left-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-bottomleft: 0px;
        border-top-left-radius: 0px;
        border-bottom-left-radius: 0px;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;
      }

      .ktv2-widget.widget-left .ktv2-widget-button {
        position: absolute;
        width:40px;
        height: 658px;
        top: 0;
        right: -40px;
        -webkit-border-top-right-radius: 8px;
        -webkit-border-bottom-right-radius: 8px;
        -moz-border-radius-topright: 8px;
        -moz-border-radius-bottomright: 8px;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
      }

      @-moz-document url-prefix() {
        .ktv2-widget.widget-left .ktv2-widget-button {
          height: calc(658px + 20px);
        }
        .ktv2-widget.widget-right .ktv2-widget-button {
          height: calc(658px + 20px)!important;
        }
      }

      .ktv2-widget.widget-right .ktv2-widget-button {
        position: absolute;
        width:40px;
        height: 658px;
        top: 0;
        left: -40px;
        -webkit-border-top-left-radius: 8px;
        -webkit-border-bottom-left-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-bottomleft: 8px;
        border-top-left-radius: 8px;
        border-bottom-left-radius: 8px;
      }

      .ktv2-widget.widget-left .ktv2-widget-button-text,
      .ktv2-widget.widget-right .ktv2-widget-button-text {
        position: absolute;
        left: -299px;
        top: 329px;
        transform: rotate(-90deg);
        width:  638px;
        padding: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      .ktv2-widget.widget-right .ktv2-widget-button-text {
        transform: rotate(90deg);
        top: 299px;
      }

      .ktv2-widget.widget-left .ktv2-caret {
        position: absolute;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        border-left: 6px dashed #ffffff;
        display: block;
        height: 0;
        width: 0;
        top: 20px;
        left: 20px;
      }

      .ktv2-widget.widget-right .ktv2-caret {
        position: absolute;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        border-right: 6px dashed #ffffff;
        display: block;
        height: 0;
        width: 0;
        bottom: 20px;
        left: 20px;
      }

    }


    @media (max-width: 380px) {

      .ktv2-widget.widget-left {
        left: 5px;
        bottom: -658px;
      }

      .ktv2-widget.widget-right {
        right: 5px;
        bottom: -658px;
      }

      .ktv2-widget.widget-bottom-left {
        left: 5px;
      }

      .ktv2-widget.widget-bottom-right {
        right: 5px;
      }

      .ktv2-widget.widget-left.ktv2-open-form,
      .ktv2-widget.widget-right.ktv2-open-form {
        animation-name: slide-out;
        animation-duration: 1s;
        bottom: 0;
      }

      .ktv2-widget.widget-left.ktv2-open-form.ktv2-close-form .ktv2-widget-body,
      .ktv2-widget.widget-right.ktv2-open-form.ktv2-close-form .ktv2-widget-body {
        animation-name: border-in;
        animation-duration: 1s;
        -webkit-border-top-left-radius: 0px;
        -webkit-border-top-right-radius: 0px;
        -moz-border-radius-topleft: 0px;
        -moz-border-radius-topright: 0px;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;
      }

      .ktv2-widget.widget-left.ktv2-open-form .ktv2-widget-body,
      .ktv2-widget.widget-right.ktv2-open-form .ktv2-widget-body {
        animation-name: border-out;
        animation-duration: 1s;
        -webkit-border-top-left-radius: 8px;
        -webkit-border-top-right-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-topright: 8px;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
      }

      .ktv2-widget.widget-left.ktv2-open-form.ktv2-close-form,
      .ktv2-widget.widget-right.ktv2-open-form.ktv2-close-form {
        animation-name: slide-in;
        animation-duration: 1s;
        bottom: -658px;
      }

      .ktv2-widget.widget-left .ktv2-widget-button,
      .ktv2-widget.widget-right .ktv2-widget-button {
        -webkit-border-top-left-radius: 8px;
        -webkit-border-top-right-radius: 8px;
        -moz-border-radius-topleft: 8px;
        -moz-border-radius-topright: 8px;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
      }

      .ktv2-widget.widget-left .ktv2-widget-button-text,
      .ktv2-widget.widget-right .ktv2-widget-button-text {
        font-size: 14px !important;
        font-weight: bold !important;
        letter-spacing: 0 !important;
        line-height: 16px !important;
        margin: 0 !important;
        padding: 10px 20px !important;
        text-align: left !important;
        cursor: pointer;
      }

      .ktv2-widget.widget-left .ktv2-caret,
      .ktv2-widget.widget-right .ktv2-caret {
        position: absolute;
        border-left: 6px solid transparent;
        border-right: 6px solid transparent;
        border-bottom: 6px dashed #ffffff;
        display: block;
        height: 0;
        width: 0;
        right: 10px;
        top: 50%;
      }

    }

    .ktv2-widget.widget-bottom-left.ktv2-open-form .ktv2-widget-body,
    .ktv2-widget.widget-bottom-right.ktv2-open-form .ktv2-widget-body {
      animation-name: border-out;
      animation-duration: 1s;
      -webkit-border-top-left-radius: 8px;
      -webkit-border-top-right-radius: 8px;
      -moz-border-radius-topleft: 8px;
      -moz-border-radius-topright: 8px;
      border-top-left-radius: 8px;
      border-top-right-radius: 8px;
    }

    .ktv2-widget.ktv2-open-form .ktv2-widget-button {
      animation-name: hide-button;
      animation-duration: 1s;
      opacity: 0;
    }

    .ktv2-widget.widget-bottom-left.ktv2-open-form.ktv2-close-form,
    .ktv2-widget.widget-bottom-right.ktv2-open-form.ktv2-close-form {
      animation-name: slide-in;
      animation-duration: 1s;
      bottom: -658px;
    }

    .ktv2-widget .ktv2-widget-button,
    .ktv2-widget .ktv2-widget-button {
      position:relative;
      width:350px;
      padding:5px;
      opacity: 1;
      -webkit-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
      -moz-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
      box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
      -moz-user-select: none;
      cursor: pointer;
    }

    .ktv2-widget.widget-bottom-left .ktv2-widget-button,
    .ktv2-widget.widget-bottom-right .ktv2-widget-button {
      -webkit-border-top-left-radius: 8px;
      -webkit-border-top-right-radius: 8px;
      -moz-border-radius-topleft: 8px;
      -moz-border-radius-topright: 8px;
      border-top-left-radius: 8px;
      border-top-right-radius: 8px;
    }

    .ktv2-widget.ktv2-open-form.ktv2-close-form .ktv2-widget-button {
      animation-name: show-button;
      animation-duration: 1s;
      opacity: 1;
    }

    .ktv2-widget.ktv2-open-form .ktv2-widget-button {
      opacity: 0;
      -webkit-box-shadow: none;
      -moz-box-shadow: none;
      box-shadow: none;
    }

    .ktv2-widget.ktv2-open-form.ktv2-close-form .ktv2-widget-button {
      opacity: 1;
      -webkit-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
      -moz-box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
      box-shadow: 0 0 20px 0 rgba(0,0,0,0.25);
    }

    .ktv2-widget-button-text {
      font-size: 14px !important;
      font-weight: bold !important;
      letter-spacing: 0 !important;
      line-height: 16px !important;
      margin: 0 !important;
      padding: 10px 20px !important;
      text-align: left !important;
      cursor: pointer;
    }

    .ktv2-widget .kt-affiliate-link a,
    .ktv2-widget .kt-affiliate-link {
      color: inherit !important;
      font-size: 14px !important;
      font-weight: normal !important;
      letter-spacing: 0 !important;
      line-height: 16px !important;
      margin: 0 !important;
      padding: 0 !important;
      text-align: left !important;
      text-decoration: underline !important;
    }

    .ktv2-widget .kt-affiliate-link a:hover {
      color: inherit !important;
      font-size: 14px !important;
      font-weight: normal !important;
      letter-spacing: 0 !important;
      line-height: 16px !important;
      margin: 0 !important;
      padding: 0 !important;
      text-align: left !important;
      text-decoration: underline !important;
    }

    .ktv2-widget .kt-affiliate-link {
      color: inherit !important;
      padding: 10px 20px !important;
      text-align: center !important;
      text-decoration: none !important;
    }

    .ktv2-widget-closer {
      position: absolute;
      top:6px;
      right:10px;
      font-size:24px;
      color:#333333;
      cursor:pointer;
      opacity: 0.8;
    }

    .ktv2-widget-closer:hover {
      opacity: 1;
    }

    .ktv2-widget.widget-bottom-left .ktv2-caret,
    .ktv2-widget.widget-bottom-right .ktv2-caret {
      position: absolute;
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-bottom: 6px dashed #ffffff;
      display: block;
      height: 0;
      width: 0;
      right: 10px;
      top: 50%;
    }

  </style>

  <script type="text/javascript">

    function ktv2OpenForm(id) {

      var form = document.getElementById('ktv2-widget-' + id);

      if ( form.classList ) {
        form.classList.remove('ktv2-open-form');
        form.classList.remove('ktv2-close-form');
        form.classList.add('ktv2-open-form');
      }
      else {
        form.className = form.className.replace('ktv2-open-form', '');
        form.className = form.className.replace('ktv2-close-form', '');
        form.className = form.className + ' ktv2-open-form';
      }
    }

    function ktv2CloseForm(id) {

      var form = document.getElementById('ktv2-widget-' + id);

      if ( form.classList ) {
        form.classList.add('ktv2-close-form');
      }
      else {
        form.className = form.className + ' ktv2-close-form';
      }
    }

  </script>

      <div id="ktv2-widget-172537" class="ktv2-widget widget-bottom-right">
        <div class="ktv2-widget-button" style="background-color:#dc0000;" onclick="ktv2OpenForm(172537);">
          <div class="ktv2-widget-button-text" style="color:#ffffff;"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ARRANGE AN APPOINTMENT FOR CONSULTATION</font></font></div>
          <div class="ktv2-caret"></div>
        </div>
        <div class="ktv2-widget-body" style="background-color:#dc0000;">
          <iframe class="ktv2" src="https://assets.klicktipp.com/userimages/112764/forms/172537/40tmz2m1tz8z57f3.html" style="position:relative;display:inline-block;width:340px;height:607px;border:0;background:transparent none no-repeat scroll 0 0;margin:0;padding:0;" width="340" height="607" scrolling="no"></iframe>
          <div class="ktv2-widget-closer" style="color:#dc0000;" onclick="ktv2CloseForm(172537);"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">×</font></font></div>
          <div class="ktv2-widget-afflink" style="color:#ffffff;"></div>
          <div class="ktv2-widget-afflink ktv2-widget-dpo" style="color:#ffffff;"><div class="kt-affiliate-link" style="position:relative;display:block;margin:5px 0 0 0;text-align:center;font-size:11px;line-height:14px;background:none;color:#999999;white-space:nowrap;"><a href="https://www.enerix.de/footer/datenschutz/" target="_blank" title="enerix Datenschutzbestimmung" style="position:relative;display:inline-block;text-decoration:none;font-size: 11px;line-height: 14px;background-color:transparent;white-space:normal;">enerix Datenschutzbestimmung</a></div></div>
        </div>
      </div>

    <div id="c1971" class="frame frame-default frame-type-enerix_threecolumn frame-layout-0"><div class="row    "><div class="col-sm-4   "><div id="c1969" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p class="h4">enerix – Smarter Energiemix</p><p>Zentral ist out, dezentral ist in. enerix liefert den smarten Energiemix, zum Selbermachen, für Menschen mit Köpfchen und&nbsp; Begeisterung für moderne Technik.&nbsp;enerix – Strom einfach selber machen, speichern und sparen.</p></div></div></div><div id="c12153" class="frame frame-default frame-type-html frame-layout-0"><div class="pe-richsnippets"><!-- 3600/3600 --><a id="pe_rating" title="Kundenbewertungen &amp; Erfahrungen zu enerix - Alternative Energietechnik. Mehr Infos anzeigen." target="_blank" href="https://www.provenexpert.com/enerix-alternative-energietechnik/" class="pe_g pe_b"> <span id="pe_name"> <span>enerix - Alternative Energietechnik</span> </span> <span> <span id="pe_stars"> <span style="width: 90%;"> <span></span> hat <span><span>4,72</span> von <span>5</span> Sternen<span></span></span> </span> </span> <span class="pe_u"> <span>20216</span> Bewertungen auf ProvenExpert.com </span> </span> </a> <script type="application/ld+json"> {"@context":"https://schema.org/","@type":"Product","name":"enerix - Alternative Energietechnik","description":"Photovoltaik, Stromspeicher, Stromcloud, Elektromobilität, PV, Solaranlage","image":"https://images.provenexpert.com/74/31/1ea90dfc2e1b4cc32119bc797414/enerix-alternative-energietechnik_full_1539661810.jpg","aggregateRating":{"@type":"AggregateRating","reviewCount":20216,"ratingValue":4.72,"bestRating":5,"worstRating":1}}</script> </div><script type="text/javascript" src="https://www.provenexpert.com/widget/richsnippet.js?u=18Tp1HGp2Z3ZjRmA1HQZ0VKA48TA1LmA&amp;v=2" async="" defer=""></script></div><div id="c20126" class="frame frame-default frame-type-div frame-layout-0"><hr class="ce-div"></div><div id="c37335" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="4" data-ce-images="4"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><a href="https://de-de.facebook.com/enerix/" title="enerix auf facebook" target="_blank" rel="noreferrer"><img class="image-embed-item" title="enerix auf facebook" alt="enerix auf facebook" src="/fileadmin/_processed_/9/3/csm_enerix_facebook_55063e5387.png" width="75" height="75" loading="lazy"></a></figure></div><div class="ce-column"><figure class="image"><a href="https://www.instagram.com/enerix_official/" title="enerix auf instagram" target="_blank" rel="noreferrer"><img class="image-embed-item" title="enerix auf instagram" alt="enerix auf instagram" src="/fileadmin/_processed_/6/a/csm_enerix_instagram_e02dd5fe63.png" width="75" height="75" loading="lazy"></a></figure></div><div class="ce-column"><figure class="image"><a href="http://linkedin.com/company/enerix-franchise-gmbh" title="enerix auf linkedin" target="_blank" rel="noreferrer"><img class="image-embed-item" title="enerix auf linkedin" alt="enerix auf linkedin" src="/fileadmin/_processed_/9/2/csm_enerix_linkedin_77e0e8d993.png" width="75" height="75" loading="lazy"></a></figure></div><div class="ce-column"><figure class="image"><a href="https://www.youtube.com/channel/UCecOkAJsQ94ZTIbw21L8u4w" title="enerix auf youtube" target="_blank" rel="noreferrer"><img class="image-embed-item" title="enerix auf youtube" alt="enerix auf youtube" src="/fileadmin/_processed_/c/d/csm_enerix_youtube_ca4ced42d2.png" width="75" height="75" loading="lazy"></a></figure></div></div></div></div></div></div></div><div id="c20127" class="frame frame-default frame-type-div frame-layout-0"><hr class="ce-div"></div><div id="c1968" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-center ce-above"><div class="ce-gallery imageorient-0" data-ce-columns="1" data-ce-images="1"><div class="ce-outer"><div class="ce-inner"><div class="ce-row"><div class="ce-column"><figure class="image"><img class="image-embed-item" title="Vollmitglied beim Deutschen Franchiseverband" alt="Vollmitglied beim Deutschen Franchiseverband" src="/fileadmin/user_upload/DFV_Siegel_RGB_170217.png" width="123" height="123" loading="lazy"></figure></div></div></div></div></div></div></div></div><div class="col-sm-4   "><div id="c5026" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p class="h4">Solar-News</p></div></div></div><div id="c1966" class="frame frame-default frame-type-list frame-layout-0"><div class="news"><div class="news-list-view newsStyle-100"><ul class="simplenews"><!--
	=====================
		Partials/List/Simple/Item.html
--><li><p><a class="light-green" title="enerix deutschlandweit auf Platz 3" target="_self" href="/blog/artikel/enerix-deutschlandweit-auf-platz-3"><span class="fa fa-angle-right" aria-hidden="true"></span>	enerix deutschlandweit auf Platz 3
    			</a></p></li></ul><ul class="simplenews"><!--
	=====================
		Partials/List/Simple/Item.html
--><li><p><a class="light-green" title="Bundesregierung verlängert die Sommerzeit" target="_self" href="/blog/artikel/bundesregierung-verlaengert-sommerzeit"><span class="fa fa-angle-right" aria-hidden="true"></span>	Bundesregierung verlängert die Sommerzeit
    			</a></p></li></ul><ul class="simplenews"><!--
	=====================
		Partials/List/Simple/Item.html
--><li><p><a class="light-green" title="Deutschland beschleunigt Photovoltaik-Ausbau" target="_self" href="/blog/artikel/deutschland-beschleunigt-photovoltaik-ausbau"><span class="fa fa-angle-right" aria-hidden="true"></span>	Deutschland beschleunigt Photovoltaik-Ausbau
    			</a></p></li></ul><ul class="simplenews"><!--
	=====================
		Partials/List/Simple/Item.html
--><li><p><a class="light-green" title="600 Millionen Euro Förderung für Solaranlagen in Österreich" target="_self" href="/blog/artikel/600-millionen-euro-foerderung-fuer-photovoltaikanlagen-in-oesterreich"><span class="fa fa-angle-right" aria-hidden="true"></span>	600 Millionen Euro Förderung für Solaranlagen in Österreich
    			</a></p></li></ul><ul class="simplenews"><!--
	=====================
		Partials/List/Simple/Item.html
--><li><p><a class="light-green" title="Infrarotheizungen - Heizen mit Solarstrom" target="_self" href="/blog/artikel/infrarotheizungen-heizen-mit-solarstrom"><span class="fa fa-angle-right" aria-hidden="true"></span>	Infrarotheizungen - Heizen mit Solarstrom
    			</a></p></li></ul></div></div></div></div><div class="col-sm-4   "><div id="c20128" class="frame frame-default frame-type-textmedia frame-layout-0"><div class="ce-textpic ce-right ce-intext"><div class="ce-bodytext"><p>Unsere Markenprodukte</p><p><strong>Photovoltaikmodule</strong></p><ul><li><a href="/produkte/photovoltaikanlagen/aleo" title="Opens internal link in current window" target="_self">aleo</a></li><li><a href="/produkte/photovoltaikanlagen/q-cells-module" title="Opens internal link in current window" target="_self" class="internal-link">Q Cells </a></li><li><a href="/produkte/photovoltaikanlagen/solarwatt" title="Opens internal link in current window" target="_self" class="internal-link">Solarwatt</a></li><li><a href="/produkte/photovoltaikanlagen/heckert" title="Opens internal link in current window" target="_self" class="internal-link">Heckert</a></li><li><a href="/produkte/photovoltaikanlagen/solarfabrik" title="Solarfabrik" target="_self">Solarfabrik</a></li></ul><p><strong>Wechselrichter</strong></p><ul><li><a href="/produkte/photovoltaikanlagen/fronius" title="Opens internal link in current window" target="_self" class="internal-link">Fronius</a></li><li><a href="/produkte/photovoltaikanlagen/solaredge" title="Opens internal link in current window" target="_self" class="internal-link">SolarEdge</a></li><li><a href="/mikrowechselrichter/enphase" target="_self">Enphase</a></li></ul><p><strong>Stromspeicher</strong></p><ul><li><a href="/produkte/solarstromspeicher/senec" title="SENEC" target="_self" class="internal-link">SENEC</a></li><li><a href="/produkte/solarstromspeicher/sonnenbatterie" title="SonnenBatterie" target="_self" class="internal-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">solar battery</font></font></a></li><li><a href="/produkte/solarstromspeicher/rct-power" title="RCT Power" target="_self" class="internal-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">RCT Power</font></font></a></li><li><a href="/produkte/solarstromspeicher/e3dc" title="E3/DC" target="_self" class="internal-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">E3/DC</font></font></a></li><li><a href="/produkte/solarstromspeicher/fenecon" title="FENECON" target="_self" class="internal-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">FENECON</font></font></a></li><li><a href="/produkte/solarstromspeicher/battery-flex" title="Solarwatt" target="_self" class="internal-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">solar watts</font></font></a></li><li><a href="/produkte/solarstromspeicher/neoom" title="neoom" target="_self" class="internal-link"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">neoom</font></font></a></li><li><a href="/produkte/solarstromspeicher/qcells" title="QCells Speicher" target="_self"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">QCells</font></font></a></li></ul></div></div></div></div></div></div></div></footer><div class="legal"><div class="container"><div class="row"><div class="col-md-6 col-sm-12 ps-0"><ul class="footermenu p-0 float-start"><li><a href="/service/newsletter" title="Photovoltaik Newsletter - Immer gut informiert sein!"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Newsletter</font></font></a></li><li><a href="/ueber-enerix/presse" title="Presse enerix - Bilder, Grafiken &amp; Interviewanfragen"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Press</font></font></a></li><li><a href="/impressum" title="Impressum - Wer hinter der tollen enerix-Seite steht!"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">imprint</font></font></a></li><li><a href="/datenschutz" title="Datenschutz - Wir halten uns an die DSGVO"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">data protection</font></font></a></li><li class="sub"><a href="/footer/login" title="Login - Sorry, Eintritt nur für enerix-Partner" class="sub"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Log in</font></font></a></li></ul></div><div class="col-md-6 col-sm-12 text-right"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                        © 2023 Enerix® Franchise GmbH &amp; Co KG
                    </font></font></div></div></div></div></div></div><a id="top-link" href="#top-position" style="display: none;"><i class="fa fa-chevron-up" aria-hidden="true"></i></a>
<script src="/typo3temp/assets/compressed/merged-c49b6c3da1e3b3da4296a70ca6423557-3c906225204c420def051be2122db3a3.js.1660289911.gzip"></script>

<script src="/typo3temp/assets/compressed/merged-88173e3bd1631a665e3c3d18b5936642-b829cbc84f08774eda1e2f8f73fa6984.js.1683094594.gzip"></script>


      <script data-cookieconsent="statistics" type="text/plain" data-ignore="1">
           window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
           ga('create', 'UA-17911350-1', 'auto');
           ga('send', 'pageview');
           ga('set', 'anonymizeIp', true);
      </script>

<script type="text/plain" data-ignore="1" data-dp-cookiedesc="layout">
    Diese Website benutzt Cookies, die für den technischen Betrieb der Website erforderlich sind und stets gesetzt werden. Andere Cookies, um Inhalte und Anzeigen zu personalisieren und die Zugriffe auf unsere Website zu analysieren, werden nur mit Ihrer Zustimmung gesetzt. Außerdem geben wir Informationen zu Ihrer Verwendung unserer Website an unsere Partner für soziale Medien, Werbung und Analysen weiter.



</script>
<script type="text/plain" data-ignore="1" data-dp-cookieselect="layout">
    <div class="dp--cookie-check" xmlns:f="http://www.w3.org/1999/html">
    <label for="dp--cookie-require">
        <input type="hidden" name="" value="" /><input disabled="disabled" class="dp--check-box" id="dp--cookie-require" tabindex="-1" type="checkbox" name="" value="" checked="checked" />
        Notwendig
    </label>
    <label for="dp--cookie-statistics">
        <input class="dp--check-box" id="dp--cookie-statistics" tabindex="1" type="checkbox" name="" value="" checked="checked" />
        Statistiken
    </label>
    <label for="dp--cookie-marketing">
        <input class="dp--check-box" id="dp--cookie-marketing" tabindex="1" type="checkbox" name="" value="" checked="checked" />
        Marketing
    </label>
</div>

</script>
<script type="text/plain" data-ignore="1" data-dp-cookierevoke="layout">
    <div class="cc-revoke dp--revoke {{classes}}">
    <i class="dp--icon-fingerprint"></i>
    <span class="dp--hover">Cookies</span>
</div>



</script>
<script type="text/plain" data-ignore="1" data-dp-cookieiframe="layout">
    <div class="dp--overlay-inner">
    <div class="dp--overlay-header">{{notice}}</div>
    <div class="dp--overlay-description">{{desc}}</div>
    <div class="dp--overlay-button">
        <button class="db--overlay-submit" onclick="window.DPCookieConsent.forceAccept(this)" data-cookieconsent="{{type}}" >
        {{btn}}
        </button>
    </div>
</div>

</script>
<script type="text/javascript" data-ignore="1">
    window.cookieconsent_options = {
        overlay: {
            notice: true,
            box: {
                background: 'rgba(255,255,255,.97)',
                text: '#7d7d7d'
            },
            btn: {
                background: '#b81839',
                text: '#fff'
            }
        },
        content: {
            message:'Diese Website benutzt Cookies, die für den technischen Betrieb der Website erforderlich sind und stets gesetzt werden. Andere Cookies, um Inhalte und Anzeigen zu personalisieren und die Zugriffe auf unsere Website zu analysieren, werden nur mit Ihrer Zustimmung gesetzt. Außerdem geben wir Informationen zu Ihrer Verwendung unserer Website an unsere Partner für soziale Medien, Werbung und Analysen weiter.',
            dismiss:'Cookies zulassen!',
            allow:'Speichern',
            deny: 'Ablehnen',
            link:'Mehr Infos',
            href:'/',
            target:'_blank',
            'allow-all': 'alle akzeptieren!',

            media: {
                notice: 'Cookie-Hinweis',
                desc: 'Durch das Laden dieser Ressource wird eine Verbindung zu externen Servern hergestellt, die Cookies und andere Tracking-Technologien verwenden, um die Benutzererfahrung zu personalisieren und zu verbessern. Weitere Informationen finden Sie in unserer Datenschutzerklärung.',
                btn: 'Erlaube Cookies und lade diese Ressource',
            }
        },
        theme: 'edgeless',
        position: 'bottom-left',
        type: 'opt-in',
        revokable: true,
        reloadOnRevoke: true,
        checkboxes: {"statistics":"true","marketing":"true"},
        palette: {
            popup: {
                background: 'rgba(255,255,255,.97)',
                text: '#7d7d7d'
            },
            button: {
                background: '#a3d20b',
                text: '#fff',
            }
        }
    };
</script>






<script src="https://www.provenexpert.com/js/lib/pejquery.js"></script>            <div id="goog-gt-" class="skiptranslate VIpgJd-yAWNEb-L7lbkb" dir="ltr"><div style="padding: 8px;"><div><div class="VIpgJd-yAWNEb-l4eHX"><img src="https://www.gstatic.com/images/branding/product/1x/translate_24dp.png" width="20" height="20" alt="Google Translate"></div></div></div><div style="padding: 8px; float: left; width: 100%;"><h1 class="VIpgJd-yAWNEb-r4nke VIpgJd-yAWNEb-mrxPge">Original text</h1></div><div style="padding: 8px;"><div class="VIpgJd-yAWNEb-nVMfcd-fmcmS"></div></div><div class="VIpgJd-yAWNEb-cGMI2b" style="padding: 8px;"><div class="VIpgJd-yAWNEb-Z0Arqf-PLDbbf"><span class="VIpgJd-yAWNEb-Z0Arqf-hSRGPd">Contribute a better translation</span></div><div class="VIpgJd-yAWNEb-fw42Ze-Z0Arqf-haAclf"><hr style="color: #ccc; background-color: #ccc; height: 1px; border: none;"><div class="VIpgJd-yAWNEb-Z0Arqf-H9tDt"></div></div></div><div class="VIpgJd-yAWNEb-jOfkMb-Ne3sFf" style="display: none;"></div></div><div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">                <div class="pswp__bg"></div>                <div class="pswp__scroll-wrap">                    <div class="pswp__container">                        <div class="pswp__item"></div>                        <div class="pswp__item"></div>                        <div class="pswp__item"></div>                    </div>                    <div class="pswp__ui pswp__ui--hidden">                        <div class="pswp__top-bar">                            <div class="pswp__counter"></div>                            <button class="pswp__button pswp__button--close" title="Close (Esc)"></button>                            <button class="pswp__button pswp__button--share" title="Share"></button>                            <button class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button>                            <button class="pswp__button pswp__button--zoom" title="Zoom in/out"></button>                            <div class="pswp__preloader">                                <div class="pswp__preloader__icn">                                    <div class="pswp__preloader__cut">                                        <div class="pswp__preloader__donut"></div>                                    </div>                                </div>                            </div>                        </div>                        <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">                            <div class="pswp__share-tooltip"></div>                         </div>                        <button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)"></button>                        <button class="pswp__button pswp__button--arrow--right" title="Next (arrow right)"></button>                        <div class="pswp__caption">                            <div class="pswp__caption__center"></div>                        </div>                    </div>                </div>            </div><div id="automa-palette"></div><div class="cc-revoke dp--revoke cc-bottom-left cc-type-opt-in cc-theme-edgeless cc-hide" style="background-color: rgba(255, 255, 255, 0.97); color: rgb(125, 125, 125);">
    <i class="dp--icon-fingerprint"></i>
    <span class="dp--hover"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">cookies</font></font></span>
</div><div aria-describedby="cookieconsent:desc" aria-label="cookieconsent" aria-live="polite" class="cc-window cc-bottom-left cc-type-opt-in cc-theme-edgeless" id="cookieconsent:window" role="dialog" style="background-color: rgba(255, 255, 255, 0.97); color: rgb(125, 125, 125);"><div class="cc-body" id="cookieconsent:body"> <span class="cc-message" id="cookieconsent:desc"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> 
    This website uses cookies, which are required for the technical operation of the website and are always set. </font><font style="vertical-align: inherit;">Other cookies to personalize content and ads and to analyze access to our website are only set with your consent. </font><font style="vertical-align: inherit;">We also share information about your use of our website with our social media, advertising and analytics partners.



 
    </font></font><div class="dp--cookie-check" xmlns:f="http://www.w3.org/1999/html">
    <label for="dp--cookie-require">
        <input type="hidden" name="" value=""><input disabled="disabled" class="dp--check-box" id="dp--cookie-require" tabindex="-1" type="checkbox" name="" value="" checked="checked"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        Necessary
    </font></font></label>
    <label for="dp--cookie-statistics">
        <input class="dp--check-box" id="dp--cookie-statistics" tabindex="1" type="checkbox" name="" value="" checked="checked"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        statistics
    </font></font></label>
    <label for="dp--cookie-marketing">
        <input class="dp--check-box" id="dp--cookie-marketing" tabindex="1" type="checkbox" name="" value="" checked="checked"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        marketing
    </font></font></label>
</div>

 </span> <div class="cc-compliance cc-highlight"> <a href="javascript:void(0)" class="cc-btn cc-allow-all cc-w-100" role="button" tabindex="2" style="background-color: rgb(163, 210, 11); color: rgb(255, 255, 255);"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">accept all!</font></font></a>  <a href="javascript:void(0)" class="cc-btn cc-allow" role="button" tabindex="2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Save on computer</font></font></a>  <a href="javascript:void(0)" class="cc-btn cc-deny" role="button" tabindex="2"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Reject</font></font></a>  </div> </div></div></body></html>
"""

result = html_parsing_tools.html_contents(html)
print(result)

# for key, values in result.items():
#     if key != "all":
#         print(key, values)


# print(
#     list(
#         map(
#             lambda x: x.strip(),
#             filter(
#                 lambda x: x.strip(),
#                 result["all"][0].replace("\n", " ").replace("\t", " ").split("  "),
#             ),
#         )
#     )
# )
