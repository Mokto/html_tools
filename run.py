from html_parsing_tools import html_parsing_tools
from sympy import false

html = """
<html lang="en"><head><style>.hs-cta-wrapper p, .hs-cta-wrapper div { margin: 0; padding: 0; } a#cta_button_8667013_ab1f6d1b-bf99-4cbd-9993-d291c17726f4 {
    -webkit-font-smoothing: antialiased;
cursor: pointer;
-moz-user-select: none;
-webkit-user-select: none;
-o-user-select: none;
user-select: none;
display: inline-block;
font-weight: normal;
text-align: center;
text-decoration: none;
-moz-transition: all .4s ease;
-webkit-transition: all .4s ease;
-o-transition: all .4s ease;
background: rgb(255,180,51);
border-radius: 6px;
border-width: 0px;
color: rgb(255,255,255);
font-family: sans-serif;
height: auto;
transition: all .4s ease;
padding: 6px 24px;
text-shadow: none;
width: auto;
font-size: 24px;
line-height: 1.5em;

    font-family: 'Poppins', sans-serif;
  }

a#cta_button_8667013_ab1f6d1b-bf99-4cbd-9993-d291c17726f4:hover {
background: rgb(255,198,56);
color: rgb(255,255,255);
}

a#cta_button_8667013_ab1f6d1b-bf99-4cbd-9993-d291c17726f4:active, #cta_button_8667013_ab1f6d1b-bf99-4cbd-9993-d291c17726f4:active:hover {
background: rgb(204,144,40);
color: rgb(244,244,244);
}

</style>
    <meta charset="utf-8">
    <title>Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales</title>
    <link rel="shortcut icon" href="https://www.ocean.io/hubfs/Logomark%20%E2%80%93%20Positive-1.png">
    <meta name="description" content="A smarter prospecting data platform that brings you 5x more high quality leads for faster, more efficient revenue growth.">
        
      
        
        
      
        
        
      <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">
      
    
    
    
    

    
    <meta property="og:description" content="A smarter prospecting data platform that brings you 5x more high quality leads for faster, more efficient revenue growth.">
    <meta property="og:title" content="Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales">
    <meta name="twitter:description" content="A smarter prospecting data platform that brings you 5x more high quality leads for faster, more efficient revenue growth.">
    <meta name="twitter:title" content="Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales">

    

    
<!-- Basic Schema  -->
<script async="true" src="https://tr.snapchat.com/config/io/e28560a8-8921-4c95-a806-263702bfcf60.js" crossorigin="anonymous"></script><script type="text/javascript" async="" src="https://snap.licdn.com/li.lms-analytics/insight.min.js"></script><script async="" src="https://www.clarity.ms/eus2-d/s/0.7.2/clarity.js"></script><script async="" src="https://www.clarity.ms/tag/uet/27035405"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-M3TVNDT"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script src="https://js.usemessages.com/conversations-embed.js" type="text/javascript" id="hubspot-messages-loader" data-loader="hs-scriptloader" data-hsjs-portal="8667013" data-hsjs-env="prod" data-hsjs-hublet="na1"></script><script src="https://js.hsadspixel.net/fb.js" type="text/javascript" id="hs-ads-pixel-8667013" data-ads-portal-id="8667013" data-ads-env="prod" data-loader="hs-scriptloader" data-hsjs-portal="8667013" data-hsjs-env="prod" data-hsjs-hublet="na1"></script><script src="https://js.hscollectedforms.net/collectedforms.js" type="text/javascript" id="CollectedForms-8667013" crossorigin="anonymous" data-leadin-portal-id="8667013" data-leadin-env="prod" data-loader="hs-scriptloader" data-hsjs-portal="8667013" data-hsjs-env="prod" data-hsjs-hublet="na1"></script><script src="https://js.hs-analytics.net/analytics/1677144600000/8667013.js" type="text/javascript" id="hs-analytics"></script><script src="https://js.hs-banner.com/8667013.js" type="text/javascript" id="cookieBanner-8667013" data-cookieconsent="ignore" data-hs-ignore="true" data-loader="hs-scriptloader" data-hsjs-portal="8667013" data-hsjs-env="prod" data-hsjs-hublet="na1"></script><script src="https://js.hsleadflows.net/leadflows.js" type="text/javascript" id="LeadFlows-8667013" crossorigin="anonymous" data-leadin-portal-id="8667013" data-leadin-env="prod" data-loader="hs-scriptloader" data-hsjs-portal="8667013" data-hsjs-env="prod" data-hsjs-hublet="na1"></script><script type="text/javascript" async="" src="https://cdn.dreamdata.cloud/scripts/identify-form/v1/identify-form.min.js"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-69801J0NSH&amp;l=dataLayer&amp;cx=c"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://connect.facebook.net/en_US/fbevents.js"></script><script type="text/javascript" async="" src="https://static.ads-twitter.com/uwt.js"></script><script type="text/javascript" async="" src="https://sc-static.net/scevent.min.js"></script><script type="text/javascript" async="" src="https://www.redditstatic.com/ads/pixel.js"></script><script type="text/javascript" async="" src="https://bat.bing.com/bat.js"></script><script type="text/javascript" async="" src="https://cdn.dreamdata.cloud/scripts/analytics/v1/dreamdata.min.js"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-M3TVNDT"></script><script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Ocean.io",
        "logo": { 
            "@type": "ImageObject",
            "url": "https://f.hubspotusercontent10.net/hubfs/8667013/Logomark%20+%20Logotype%20%E2%80%93%20Positive-1.png"
        },
        "url": "https://www.ocean.io",
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "",
            "addressRegion": "Denmark",
            "addressLocality": "Copenhagen",
            "postalCode":"",
            "streetAddress": "Strandgade 4, 3rd Floor"
        },
        "knowsLanguage": "en"
    }
</script>


    <style>
a.cta_button{-moz-box-sizing:content-box !important;-webkit-box-sizing:content-box !important;box-sizing:content-box !important;vertical-align:middle}.hs-breadcrumb-menu{list-style-type:none;margin:0px 0px 0px 0px;padding:0px 0px 0px 0px}.hs-breadcrumb-menu-item{float:left;padding:10px 0px 10px 10px}.hs-breadcrumb-menu-divider:before{content:'›';padding-left:10px}.hs-featured-image-link{border:0}.hs-featured-image{float:right;margin:0 0 20px 20px;max-width:50%}@media (max-width: 568px){.hs-featured-image{float:none;margin:0;width:100%;max-width:100%}}.hs-screen-reader-text{clip:rect(1px, 1px, 1px, 1px);height:1px;overflow:hidden;position:absolute !important;width:1px}
</style>

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&amp;family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,400&amp;display=swap">
<link rel="stylesheet" href="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66455535975/1673904904846/POWER_x_OCEANIO/css/pwr.min.css">
<link rel="stylesheet" href="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66455403081/1673904917544/POWER_x_OCEANIO/css/custom-styles.min.css">
<link rel="stylesheet" href="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/67733428232/1667915059848/POWER_x_OCEANIO/oceanio.min.css">
<link rel="stylesheet" href="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/69702251600/1673904916959/POWER_x_OCEANIO/css/components/shared/scroll-shadow.css">
<link rel="stylesheet" href="https://cdn2.hubspot.net/hub/-1/hub_generated/module_assets/-35056501883/1677097379459/module_-35056501883_Video.min.css">

  <style>
    #oembed_container-widget_1663926010817 .oembed_custom-thumbnail_icon svg {
      fill: #ffffff;
    }
  </style>



                <style>
                    #shape-divider_module_16630607738162-1 {
                        
                        
                        transform: scale(-1,-1);
                            -webkit-transform: scale(-1,-1);
                        z-index:2;
                    }

                    #shape-divider_module_16630607738162-1 .pwr-shape-divider__svg {
                        height: auto;
                        width: 100%; 
                    }
                    
                </style>
                

                <style>
                    #shape-divider_module_16630607738162-2 {
                        
                        
                        transform: scale(-1,-1);
                            -webkit-transform: scale(-1,-1);
                        z-index:3;
                    }

                    #shape-divider_module_16630607738162-2 .pwr-shape-divider__svg {
                        height: auto;
                        width: 100%; 
                    }
                    
                </style>
                

            <style>
            #hs_cos_wrapper_module_16630607738162 .pwr-shape-divider__offset-wrapper { z-index:4; }

@media (min-width:576px) {
  #hs_cos_wrapper_module_16630607738162 .pwr-shape-divider__offset-wrapper {
    padding-bottom:0px;
    padding-top:0px;
  }
}

            </style>
            

    <style>
    @media (min-width:992px) {
  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__mockup {
    --margin-center:calc(22.5% - min(950px,45%)/2);
    --margin-side:calc(45% - min(950px,45%));
  }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__mockup--desktop-align-center:not(.pwr-sec-mockup__mockup--right) { margin-left:var(--margin-center); }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__mockup--desktop-align-right:not(.pwr-sec-mockup__mockup--right) { margin-left:var(--margin-side); }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__mockup--desktop-align-center.pwr-sec-mockup__mockup--right { margin-right:var(--margin-center); }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__mockup--desktop-align-left.pwr-sec-mockup__mockup--right { margin-right:var(--margin-side); }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__content { text-align:left; }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__title-intro {}

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__title-intro--has-background { margin-left:0.825em; }
}

@media (max-width:991px) {
  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__content { text-align:center; }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__title-intro {
    margin-left:auto;
    margin-right:auto;
  }

  #hs_cos_wrapper_widget_1647420016351 .pwr-sec-mockup__title-intro--has-background {}
}

    </style>


    <style>
    @media (min-width:992px) {
  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__mockup {
    --margin-center:calc(27.5% - min(950px,55%)/2);
    --margin-side:calc(55% - min(950px,55%));
  }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__mockup--desktop-align-center:not(.pwr-sec-mockup__mockup--right) { margin-left:var(--margin-center); }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__mockup--desktop-align-right:not(.pwr-sec-mockup__mockup--right) { margin-left:var(--margin-side); }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__mockup--desktop-align-center.pwr-sec-mockup__mockup--right { margin-right:var(--margin-center); }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__mockup--desktop-align-left.pwr-sec-mockup__mockup--right { margin-right:var(--margin-side); }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__content { text-align:left; }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__title-intro {}

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__title-intro--has-background { margin-left:0.825em; }
}

@media (max-width:991px) {
  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__content { text-align:center; }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__title-intro {
    margin-left:auto;
    margin-right:auto;
  }

  #hs_cos_wrapper_module_16474205290554 .pwr-sec-mockup__title-intro--has-background {}
}

    </style>


                <style>
                    #shape-divider_dnd_area-module-8-1 {
                        
                        
                        transform: scale(-1,1);
                            -webkit-transform: scale(-1,1);
                        z-index:2;
                    }

                    #shape-divider_dnd_area-module-8-1 .pwr-shape-divider__svg {
                        height: 50px;
                        width: 100%; 
                    }
                    
                    @media (max-width:575px) {
                        #shape-divider_dnd_area-module-8-1 .pwr-shape-divider__svg {
                            height: calc(50 * .6)!important;
                        }
                    }
                    
                </style>
                

            <style>
            #hs_cos_wrapper_dnd_area-module-8 .pwr-shape-divider__offset-wrapper { z-index:3; }

@media (min-width:576px) {
  #hs_cos_wrapper_dnd_area-module-8 .pwr-shape-divider__offset-wrapper {
    padding-bottom:30px;
    padding-top:0px;
  }
}

            </style>
            
<!-- Editor Styles -->
<style id="hs_editor_style" type="text/css">
#hs_cos_wrapper_module_16667035161316  { display: block !important; padding-top: 30px !important }
#hs_cos_wrapper_module_1668083053541  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_module_1668083091530  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_module_1668083072823  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_module_16768900970713  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_widget_1663927128610  { display: block !important; padding-bottom: 10px !important; padding-top: 20px !important }
#hs_cos_wrapper_module_16667035161316  { display: block !important; padding-top: 30px !important }
#hs_cos_wrapper_module_1668083053541  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_module_1668083091530  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_module_1668083072823  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_module_16768900970713  { border-radius: 0px !important; display: block !important }
#hs_cos_wrapper_widget_1663927128610  { display: block !important; padding-bottom: 10px !important; padding-top: 20px !important }
.dnd_area-row-0-background-image {
  background-image: url('https://www.ocean.io/hubfs/Frame%20153852%20%282%29.png') !important;
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
}
.dnd_area-row-1-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-2-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-3-background-color {
  background-color: rgba(244, 246, 249, 1) !important;
}
.dnd_area-row-3-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-4-background-color {
  background-color: rgba(244, 246, 249, 1) !important;
}
.dnd_area-row-8-background-color {
  background-color: rgba(244, 246, 249, 1) !important;
}
.dnd_area-row-10-background-color {
  background-color: rgba(244, 246, 249, 1) !important;
}
.dnd_area-row-13-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-14-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-15-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-16-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-17-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.dnd_area-row-19-force-full-width-section > .row-fluid {
  max-width: none !important;
}
.module_1668083053541-flexbox-positioning {
  display: -ms-flexbox !important;
  -ms-flex-direction: column !important;
  -ms-flex-align: center !important;
  -ms-flex-pack: start;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start;
}
.module_1668083053541-flexbox-positioning > div {
  max-width: 100%;
  flex-shrink: 0 !important;
}
.widget_1673860988459-flexbox-positioning {
  display: -ms-flexbox !important;
  -ms-flex-direction: column !important;
  -ms-flex-align: center !important;
  -ms-flex-pack: start;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start;
}
.widget_1673860988459-flexbox-positioning > div {
  max-width: 100%;
  flex-shrink: 0 !important;
}
.module_16600405384383-flexbox-positioning {
  display: -ms-flexbox !important;
  -ms-flex-direction: column !important;
  -ms-flex-align: center !important;
  -ms-flex-pack: start;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start;
}
.module_16600405384383-flexbox-positioning > div {
  max-width: 100%;
  flex-shrink: 0 !important;
}
.module_1668083091530-flexbox-positioning {
  display: -ms-flexbox !important;
  -ms-flex-direction: column !important;
  -ms-flex-align: center !important;
  -ms-flex-pack: start;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start;
}
.module_1668083091530-flexbox-positioning > div {
  max-width: 100%;
  flex-shrink: 0 !important;
}
.module_1668083072823-flexbox-positioning {
  display: -ms-flexbox !important;
  -ms-flex-direction: column !important;
  -ms-flex-align: center !important;
  -ms-flex-pack: start;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start;
}
.module_1668083072823-flexbox-positioning > div {
  max-width: 100%;
  flex-shrink: 0 !important;
}
.module_16768900970713-flexbox-positioning {
  display: -ms-flexbox !important;
  -ms-flex-direction: column !important;
  -ms-flex-align: center !important;
  -ms-flex-pack: start;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start;
}
.module_16768900970713-flexbox-positioning > div {
  max-width: 100%;
  flex-shrink: 0 !important;
}
/* HubSpot Non-stacked Media Query Styles */
@media (min-width:768px) {
  .cell_16667035161312-row-1-vertical-alignment > .row-fluid {
    display: -ms-flexbox !important;
    -ms-flex-direction: row;
    display: flex !important;
    flex-direction: row;
  }
  .cell_1673897328388-vertical-alignment {
    display: -ms-flexbox !important;
    -ms-flex-direction: column !important;
    -ms-flex-pack: center !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
  }
  .cell_1673897328388-vertical-alignment > div {
    flex-shrink: 0 !important;
  }
  .cell_1666703527027-vertical-alignment {
    display: -ms-flexbox !important;
    -ms-flex-direction: column !important;
    -ms-flex-pack: center !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
  }
  .cell_1666703527027-vertical-alignment > div {
    flex-shrink: 0 !important;
  }
}
/* HubSpot Styles (default) */
.dnd_area-row-0-padding {
  padding-top: 40px !important;
  padding-bottom: 80px !important;
  padding-left: 40px !important;
  padding-right: 40px !important;
}
.dnd_area-row-1-padding {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.dnd_area-row-2-padding {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.dnd_area-row-3-padding {
  padding-top: 0px !important;
  padding-bottom: 20px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.dnd_area-row-4-padding {
  padding-top: 0px !important;
  padding-bottom: 40px !important;
}
.dnd_area-row-5-padding {
  padding-top: 100px !important;
  padding-bottom: 80px !important;
}
.dnd_area-row-6-padding {
  padding-top: 0px !important;
  padding-bottom: 20px !important;
}
.dnd_area-row-7-padding {
  padding-top: 0px !important;
  padding-bottom: 100px !important;
}
.dnd_area-row-8-padding {
  padding-top: 100px !important;
  padding-bottom: 40px !important;
}
.dnd_area-row-9-padding {
  padding-top: 100px !important;
  padding-bottom: 100px !important;
}
.dnd_area-row-10-padding {
  padding-top: 100px !important;
  padding-bottom: 40px !important;
}
.dnd_area-row-11-padding {
  padding-top: 20px !important;
  padding-bottom: 30px !important;
}
.dnd_area-row-12-padding {
  padding-top: 10px !important;
  padding-bottom: 40px !important;
}
.dnd_area-row-13-padding {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.dnd_area-row-14-padding {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.dnd_area-row-15-padding {
  padding-top: 60px !important;
  padding-bottom: 20px !important;
  padding-left: 80px !important;
  padding-right: 80px !important;
}
.dnd_area-row-16-padding {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.dnd_area-row-17-padding {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.dnd_area-row-18-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
}
.dnd_area-row-19-padding {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-left: 0px !important;
  padding-right: 0px !important;
}
.widget_1666703696264-hidden {
  display: none !important;
}
.module_16738973283883-hidden {
  display: none !important;
}
.cell_1666703527027-padding {
  padding-top: 10px !important;
}
.widget_1646920243164-hidden {
  display: block !important;
}
.cell_1675779264919-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  padding-left: 20px !important;
}
.cell_16680830389655-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  padding-left: 20px !important;
}
.cell_16680830535406-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  padding-left: 20px !important;
}
.cell_16680830535405-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
}
.cell_16680830915297-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  padding-left: 20px !important;
}
.cell_16680830915296-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
}
.cell_16680830728227-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  padding-left: 20px !important;
}
.cell_16680830728226-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  padding-left: 0px !important;
}
.cell_16768900970693-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  padding-left: 20px !important;
}
.cell_16768900970692-padding {
  padding-top: 20px !important;
  padding-bottom: 20px !important;
}
.dnd_area-module-6-hidden {
  display: block !important;
}
.widget_1647420016351-hidden {
  display: none !important;
}
.module_16474205290554-hidden {
  display: none !important;
}
.dnd_area-module-8-hidden {
  display: none !important;
}
</style>

    


    
<!--  Added by GoogleAnalytics integration -->
<script>
var _hsp = window._hsp = window._hsp || [];
_hsp.push(['addPrivacyConsentListener', function(consent) { if (consent.allowed || (consent.categories && consent.categories.analytics)) {
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  ga('create','UA-132486915-1','auto');
  ga('send','pageview');
}}]);
</script>

<!-- /Added by GoogleAnalytics integration -->

<!--  Added by GoogleTagManager integration -->
<script>
var _hsp = window._hsp = window._hsp || [];

var hsLoadGtm = function loadGtm() {
    if(window._hsGtmLoadOnce) {
      return;
    }

    (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-M3TVNDT');

    window._hsGtmLoadOnce = true;
};

var useGoogleConsentMode = false;

if (!useGoogleConsentMode){
    _hsp.push(['addPrivacyConsentListener', function(consent){
      if(consent.allowed || (consent.categories && consent.categories.analytics)){
        hsLoadGtm();
      }
  }]);
} else{
    if(!window._hsGoogleConsentRunOnce){
      window._hsGoogleConsentRunOnce=true;

      window.dataLayer=window.dataLayer||[];
      function gtag(){dataLayer.push(arguments);}

      gtag('consent','default',{
        'ad_storage':'denied',
        'analytics_storage':'denied'
      });

      gtag('set','developer_id.dZTQ1Zm',true);

      _hsp.push(['addPrivacyConsentListener',function(consent){
      var hasAnalyticsConsent=consent&&(consent.allowed||(consent.categories&&consent.categories.analytics));
      var hasAdsConsent=consent&&(consent.allowed||(consent.categories&&consent.categories.advertisement));

      gtag('consent','update',{
        'ad_storage':hasAdsConsent?'granted':'denied',
        'analytics_storage':hasAnalyticsConsent?'granted':'denied'
      });
    }]);
  }

  hsLoadGtm();
}
</script>

<!-- /Added by GoogleTagManager integration -->

    <link rel="canonical" href="https://www.ocean.io">

<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="facebook-domain-verification" content="ylasiama6j96t9dp78w1fi85oq4sdz">
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-M3TVNDT');</script>
<!-- End Google Tag Manager -->
<meta property="og:image" content="https://www.ocean.io/hubfs/Frame%20153832.png#keepProtocol">
<meta property="og:image:width" content="600">
<meta property="og:image:height" content="600">

<meta name="twitter:image" content="https://www.ocean.io/hubfs/Frame%20153832.png#keepProtocol">


<meta property="og:url" content="https://www.ocean.io">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="content-language" content="en">
<link rel="alternate" hreflang="de" href="https://www.ocean.io/de/">
<link rel="alternate" hreflang="en" href="https://www.ocean.io">



<link rel="stylesheet" href="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/88388171780/1667912503404/main_page_test/child.min.css">

<meta name="facebook-domain-verification" content="xb4deo0qi53as1mjk0s1ij6rbgs6gg">
  
  <meta name="generator" content="HubSpot"><meta http-equiv="origin-trial" content="A751Xsk4ZW3DVQ8WZng2Dk5s3YzAyqncTzgv+VaE6wavgTY0QHkDvUTET1o7HanhuJO8lgv1Vvc88Ij78W1FIAAAAAB7eyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGV0YWdtYW5hZ2VyLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A751Xsk4ZW3DVQ8WZng2Dk5s3YzAyqncTzgv+VaE6wavgTY0QHkDvUTET1o7HanhuJO8lgv1Vvc88Ij78W1FIAAAAAB7eyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGV0YWdtYW5hZ2VyLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1RoaXJkUGFydHkiOnRydWV9"><script type="text/javascript" async="" src="https://googleads.g.doubleclick.net/pagead/viewthroughconversion/770268826/?random=1677144738986&amp;cv=11&amp;fst=1677144738986&amp;bg=ffffff&amp;guid=ON&amp;async=1&amp;gtm=45je32m0h2&amp;u_w=1920&amp;u_h=1080&amp;hn=www.googleadservices.com&amp;frm=0&amp;url=https%3A%2F%2Fwww.ocean.io%2F&amp;tiba=Ocean.io%20%7C%20B2B%20Prospecting%20Data%20%7C%20ABM%20Targeting%20%7C%20Vertical%20Sales&amp;auid=472590321.1676550096&amp;uaa=arm&amp;uab=64&amp;uafvl=Not_A%2520Brand%3B99.0.0.0%7CGoogle%2520Chrome%3B109.0.5414.119%7CChromium%3B109.0.5414.119&amp;uamb=0&amp;uap=macOS&amp;uapv=12.6.1&amp;uaw=0&amp;data=event%3Dgtag.config&amp;rfmt=3&amp;fmt=4"></script><script type="text/javascript" referrerpolicy="no-referrer-when-downgrade" async="" src="https://app.hubspot.com/content-tools-menu/api/v1/tools-menu/has-permission?portalId=8667013&amp;callback=jsonpHandler"></script><script src="https://bat.bing.com/p/action/27035405.js" type="text/javascript" async="" data-ueto="ueto_e77b296347"></script><style type="text/css" id="hs-form-style3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356">.fn-date-picker.pika-single{z-index:9999;display:block;position:relative;color:#333;background:#fff;border:1px solid #ccc;border-bottom-color:#bbb;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;*zoom:1}.fn-date-picker.pika-single.is-hidden{display:none}.fn-date-picker.pika-single.is-bound{position:absolute;box-shadow:0 5px 15px -5px rgba(0,0,0,.5)}.fn-date-picker.pika-single:after,.fn-date-picker.pika-single:before{content:" ";display:table}.fn-date-picker.pika-single:after{clear:both}.fn-date-picker .pika-lendar{float:left;width:240px;margin:8px}.fn-date-picker .pika-title{position:relative;text-align:center}.fn-date-picker .pika-title select{cursor:pointer;position:absolute;z-index:9998;margin:0;left:0;top:5px;filter:alpha(opacity=0);opacity:0}.fn-date-picker .pika-label{display:inline-block;*display:inline;position:relative;z-index:9999;overflow:hidden;margin:0;padding:5px 3px;font-size:14px;line-height:20px;font-weight:700;background-color:#fff}.fn-date-picker .pika-next,.fn-date-picker .pika-prev{display:block;cursor:pointer;position:relative;outline:none;border:0;padding:0;width:20px;height:30px;text-indent:20px;white-space:nowrap;overflow:hidden;background-color:transparent;background-position:50%;background-repeat:no-repeat;background-size:75% 75%;opacity:.5;*position:absolute;*top:0}.fn-date-picker .pika-next:hover,.fn-date-picker .pika-prev:hover{opacity:1}.fn-date-picker .pika-next.is-disabled,.fn-date-picker .pika-prev.is-disabled{cursor:default;opacity:.2}.fn-date-picker .is-rtl .pika-next,.fn-date-picker .pika-prev{float:left;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAeCAYAAAAsEj5rAAAAUklEQVR42u3VMQoAIBADQf8Pgj+OD9hG2CtONJB2ymQkKe0HbwAP0xucDiQWARITIDEBEnMgMQ8S8+AqBIl6kKgHiXqQqAeJepBo/z38J/U0uAHlaBkBl9I4GwAAAABJRU5ErkJggg==");*left:0}.fn-date-picker .is-rtl .pika-prev,.fn-date-picker .pika-next{float:right;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAeCAYAAAAsEj5rAAAAU0lEQVR42u3VOwoAMAgE0dwfAnNjU26bYkBCFGwfiL9VVWoO+BJ4Gf3gtsEKKoFBNTCoCAYVwaAiGNQGMUHMkjGbgjk2mIONuXo0nC8XnCf1JXgArVIZAQh5TKYAAAAASUVORK5CYII=");*right:0}.fn-date-picker .pika-select{display:inline-block;*display:inline}.fn-date-picker .pika-table{width:100%;border-collapse:collapse;border-spacing:0;border:0}.fn-date-picker .pika-table td,.fn-date-picker .pika-table th{width:14.285714285714286%;padding:0}.fn-date-picker .pika-table th{color:#999;font-size:12px;line-height:25px;font-weight:700;text-align:center}.fn-date-picker .pika-table abbr{border-bottom:none;cursor:help}.fn-date-picker .pika-button{cursor:pointer;display:block;-moz-box-sizing:border-box;box-sizing:border-box;outline:none;border:0;margin:0;width:100%;padding:5px;color:#666;font-size:12px;line-height:15px;text-align:right;background:#f5f5f5}.fn-date-picker .pika-button:hover{color:#fff!important;background:#ff8000!important;box-shadow:none!important;border-radius:3px!important}.fn-date-picker .is-today .pika-button{color:#3af;font-weight:700}.fn-date-picker .is-selected .pika-button{color:#fff;font-weight:700;background:#3af;box-shadow:inset 0 1px 3px #178fe5;border-radius:3px}.fn-date-picker .is-disabled .pika-button{pointer-events:none;cursor:default;color:#999;opacity:.3}.fn-date-picker .pika-week{font-size:11px;color:#999} .hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .inputs-list.inline-list li{vertical-align:top;display:inline-block;word-wrap:break-word;padding-right:16px}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .inputs-list.inline-list li:after{clear:both}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .inputs-list.inline-list li input{float:left}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .inputs-list.inline-list.inline-list-2 li{width:50%}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .inputs-list.inline-list.inline-list-2 li:nth-child(2n){padding-right:0}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .inputs-list.inline-list.inline-list-3 li{width:33%}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .inputs-list.inline-list.inline-list-3 li:nth-child(3n){width:34%;padding-right:0}.hs-fieldtype-intl-phone.hs-input{padding:0;background:none;border:none;height:auto}.hs-fieldtype-intl-phone.hs-input:after{clear:both;content:" ";display:table}.hs-fieldtype-intl-phone.hs-input .hs-input{margin-bottom:0}.hs-fieldtype-intl-phone.hs-input input{width:68%!important;float:right}.hs-fieldtype-intl-phone.hs-input select{float:left;width:30%!important}@media (max-device-width:480px) and (min-device-width:320px),(max-width:400px){.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356>.hs-phone>.input>.hs-fieldtype-intl-phone.hs-input>input.hs-input{width:68%!important}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356>.hs-phone>.input>.hs-fieldtype-intl-phone.hs-input>select.hs-input{width:30%!important}}.hs-fieldtype-textarea.hs-input{resize:vertical}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .hs-button{white-space:pre-wrap}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .hs-richtext{word-break:break-word}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset{border:0;padding:0;margin:0;max-width:500px}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-1 .hs-input{width:95%}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-1 .input{margin-right:8px}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-1 input[type=checkbox],.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-1 input[type=radio]{width:auto}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-2 .hs-form-field{width:50%;float:left}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-2 .input{margin-right:8px}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-3 .hs-form-field{width:32.7%;float:left}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 fieldset.form-columns-3 .input{margin-right:8px}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 label.hs-hidden{visibility:hidden}.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 .hs-field-desc{width:100%}.hs-custom-style .hs-input,.hs-custom-style fieldset{max-width:100%}.hs-custom-style>div.form-columns-3 .hs-form-field,.hs-custom-style fieldset.form-columns-3 .hs-form-field{width:33.3%}.hs-custom-style>div>div:last-of-type .hs-input:not([type=checkbox]):not([type=radio]),.hs-custom-style fieldset>div:last-of-type .hs-input:not([type=checkbox]):not([type=radio]){width:100%;max-width:100%}.hs-custom-style>div input:not([type=image]):not([type=submit]):not([type=button]):not([type=radio]):not([type=checkbox]):not([type=file]),.hs-custom-style fieldset input:not([type=image]):not([type=submit]):not([type=button]):not([type=radio]):not([type=checkbox]):not([type=file]){box-sizing:border-box;padding:0 15px;min-height:27px}.hs-custom-style>div textarea,.hs-custom-style fieldset textarea{padding:10px 15px}.hs-custom-style .hs-dependent-field>div .hs-input:not([type=checkbox]):not([type=radio]){width:100%}@media (max-width:400px),(min-device-width:320px) and (max-device-width:480px){.hs-custom-style .hs-input:not([type=checkbox]):not([type=radio]),.hs-custom-style fieldset{margin-right:0!important;width:100%!important}form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-2 .hs-form-field,form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-3 .hs-form-field{float:none;width:100%}form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-2 .hs-form-field .hs-input,form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-3 .hs-form-field .hs-input{width:95%}form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-2 .hs-form-field input[type=checkbox],form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-2 .hs-form-field input[type=radio],form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-3 .hs-form-field input[type=checkbox],form.hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356:not(.hs-video-form) .form-columns-3 .hs-form-field input[type=radio]{width:auto}}.legal-consent-container .field.hs-form-field{margin-bottom:8px}.legal-consent-container .hs-field-desc.checkbox-desc{margin:-12px 0 0 21px}.legal-consent-container .hs-form-booleancheckbox-display input{float:left}.legal-consent-container .hs-form-booleancheckbox-display>span{display:block;margin-left:20px}.legal-consent-container .hs-form-booleancheckbox-display p{margin:0;display:inline}.legal-consent-container .hs-error-msgs label{color:#f2545b}.legal-consent-container~.hs_recaptcha{margin-top:18px}.cookie-reset-container{font-size:14px;margin-bottom:10px;text-align:right}#hs-outer-captcha-target,#hs-outer-captcha-target *{display:none;height:0;width:0}.hubspot-link__container{font-size:14px;padding-bottom:40px;position:relative;color:#9fa0a2;font-family:Helvetica Neue,Helvetica,Arial,sans-serif}.hubspot-link-text{color:#00a4bd;font-weight:400}.hubspot-link__container.sproket{color:#9fa0a2}.hubspot-link{color:#9fa0a2}.hubspot-link,.hubspot-link:hover{text-decoration:none}.hubspot-link:hover .hubspot-link-text{text-decoration:underline}.hubspot-link__icon{margin-bottom:-1px;margin-right:5px}.hubspot-link__container.sproket .hubspot-link__icon{width:30px;margin-right:0;float:left;margin-top:-9px;margin-left:-5px}</style><script type="text/javascript" async="" src="/hs/cta/ctas/v2/public/cs/cta-loaded.js?pid=8667013&amp;pg=6267880d-d478-4deb-b59b-3d216840c074&amp;lt=1677144738755&amp;dt=1677144738757&amp;at=1677144739356&amp;ae=1&amp;sl=1&amp;an=1"></script><style type="text/css" id="hs-form-style4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b">.fn-date-picker.pika-single{z-index:9999;display:block;position:relative;color:#333;background:#fff;border:1px solid #ccc;border-bottom-color:#bbb;font-family:Helvetica Neue,Helvetica,Arial,sans-serif;*zoom:1}.fn-date-picker.pika-single.is-hidden{display:none}.fn-date-picker.pika-single.is-bound{position:absolute;box-shadow:0 5px 15px -5px rgba(0,0,0,.5)}.fn-date-picker.pika-single:after,.fn-date-picker.pika-single:before{content:" ";display:table}.fn-date-picker.pika-single:after{clear:both}.fn-date-picker .pika-lendar{float:left;width:240px;margin:8px}.fn-date-picker .pika-title{position:relative;text-align:center}.fn-date-picker .pika-title select{cursor:pointer;position:absolute;z-index:9998;margin:0;left:0;top:5px;filter:alpha(opacity=0);opacity:0}.fn-date-picker .pika-label{display:inline-block;*display:inline;position:relative;z-index:9999;overflow:hidden;margin:0;padding:5px 3px;font-size:14px;line-height:20px;font-weight:700;background-color:#fff}.fn-date-picker .pika-next,.fn-date-picker .pika-prev{display:block;cursor:pointer;position:relative;outline:none;border:0;padding:0;width:20px;height:30px;text-indent:20px;white-space:nowrap;overflow:hidden;background-color:transparent;background-position:50%;background-repeat:no-repeat;background-size:75% 75%;opacity:.5;*position:absolute;*top:0}.fn-date-picker .pika-next:hover,.fn-date-picker .pika-prev:hover{opacity:1}.fn-date-picker .pika-next.is-disabled,.fn-date-picker .pika-prev.is-disabled{cursor:default;opacity:.2}.fn-date-picker .is-rtl .pika-next,.fn-date-picker .pika-prev{float:left;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAeCAYAAAAsEj5rAAAAUklEQVR42u3VMQoAIBADQf8Pgj+OD9hG2CtONJB2ymQkKe0HbwAP0xucDiQWARITIDEBEnMgMQ8S8+AqBIl6kKgHiXqQqAeJepBo/z38J/U0uAHlaBkBl9I4GwAAAABJRU5ErkJggg==");*left:0}.fn-date-picker .is-rtl .pika-prev,.fn-date-picker .pika-next{float:right;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAeCAYAAAAsEj5rAAAAU0lEQVR42u3VOwoAMAgE0dwfAnNjU26bYkBCFGwfiL9VVWoO+BJ4Gf3gtsEKKoFBNTCoCAYVwaAiGNQGMUHMkjGbgjk2mIONuXo0nC8XnCf1JXgArVIZAQh5TKYAAAAASUVORK5CYII=");*right:0}.fn-date-picker .pika-select{display:inline-block;*display:inline}.fn-date-picker .pika-table{width:100%;border-collapse:collapse;border-spacing:0;border:0}.fn-date-picker .pika-table td,.fn-date-picker .pika-table th{width:14.285714285714286%;padding:0}.fn-date-picker .pika-table th{color:#999;font-size:12px;line-height:25px;font-weight:700;text-align:center}.fn-date-picker .pika-table abbr{border-bottom:none;cursor:help}.fn-date-picker .pika-button{cursor:pointer;display:block;-moz-box-sizing:border-box;box-sizing:border-box;outline:none;border:0;margin:0;width:100%;padding:5px;color:#666;font-size:12px;line-height:15px;text-align:right;background:#f5f5f5}.fn-date-picker .pika-button:hover{color:#fff!important;background:#ff8000!important;box-shadow:none!important;border-radius:3px!important}.fn-date-picker .is-today .pika-button{color:#3af;font-weight:700}.fn-date-picker .is-selected .pika-button{color:#fff;font-weight:700;background:#3af;box-shadow:inset 0 1px 3px #178fe5;border-radius:3px}.fn-date-picker .is-disabled .pika-button{pointer-events:none;cursor:default;color:#999;opacity:.3}.fn-date-picker .pika-week{font-size:11px;color:#999} .hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .inputs-list.inline-list li{vertical-align:top;display:inline-block;word-wrap:break-word;padding-right:16px}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .inputs-list.inline-list li:after{clear:both}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .inputs-list.inline-list li input{float:left}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .inputs-list.inline-list.inline-list-2 li{width:50%}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .inputs-list.inline-list.inline-list-2 li:nth-child(2n){padding-right:0}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .inputs-list.inline-list.inline-list-3 li{width:33%}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .inputs-list.inline-list.inline-list-3 li:nth-child(3n){width:34%;padding-right:0}.hs-fieldtype-intl-phone.hs-input{padding:0;background:none;border:none;height:auto}.hs-fieldtype-intl-phone.hs-input:after{clear:both;content:" ";display:table}.hs-fieldtype-intl-phone.hs-input .hs-input{margin-bottom:0}.hs-fieldtype-intl-phone.hs-input input{width:68%!important;float:right}.hs-fieldtype-intl-phone.hs-input select{float:left;width:30%!important}@media (max-device-width:480px) and (min-device-width:320px),(max-width:400px){.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b>.hs-phone>.input>.hs-fieldtype-intl-phone.hs-input>input.hs-input{width:68%!important}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b>.hs-phone>.input>.hs-fieldtype-intl-phone.hs-input>select.hs-input{width:30%!important}}.hs-fieldtype-textarea.hs-input{resize:vertical}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .hs-button{white-space:pre-wrap}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .hs-richtext{word-break:break-word}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset{border:0;padding:0;margin:0;max-width:500px}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-1 .hs-input{width:95%}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-1 .input{margin-right:8px}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-1 input[type=checkbox],.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-1 input[type=radio]{width:auto}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-2 .hs-form-field{width:50%;float:left}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-2 .input{margin-right:8px}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-3 .hs-form-field{width:32.7%;float:left}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b fieldset.form-columns-3 .input{margin-right:8px}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b label.hs-hidden{visibility:hidden}.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b .hs-field-desc{width:100%}.hs-custom-style .hs-input,.hs-custom-style fieldset{max-width:100%}.hs-custom-style>div.form-columns-3 .hs-form-field,.hs-custom-style fieldset.form-columns-3 .hs-form-field{width:33.3%}.hs-custom-style>div>div:last-of-type .hs-input:not([type=checkbox]):not([type=radio]),.hs-custom-style fieldset>div:last-of-type .hs-input:not([type=checkbox]):not([type=radio]){width:100%;max-width:100%}.hs-custom-style>div input:not([type=image]):not([type=submit]):not([type=button]):not([type=radio]):not([type=checkbox]):not([type=file]),.hs-custom-style fieldset input:not([type=image]):not([type=submit]):not([type=button]):not([type=radio]):not([type=checkbox]):not([type=file]){box-sizing:border-box;padding:0 15px;min-height:27px}.hs-custom-style>div textarea,.hs-custom-style fieldset textarea{padding:10px 15px}.hs-custom-style .hs-dependent-field>div .hs-input:not([type=checkbox]):not([type=radio]){width:100%}@media (max-width:400px),(min-device-width:320px) and (max-device-width:480px){.hs-custom-style .hs-input:not([type=checkbox]):not([type=radio]),.hs-custom-style fieldset{margin-right:0!important;width:100%!important}form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-2 .hs-form-field,form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-3 .hs-form-field{float:none;width:100%}form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-2 .hs-form-field .hs-input,form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-3 .hs-form-field .hs-input{width:95%}form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-2 .hs-form-field input[type=checkbox],form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-2 .hs-form-field input[type=radio],form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-3 .hs-form-field input[type=checkbox],form.hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b:not(.hs-video-form) .form-columns-3 .hs-form-field input[type=radio]{width:auto}}.legal-consent-container .field.hs-form-field{margin-bottom:8px}.legal-consent-container .hs-field-desc.checkbox-desc{margin:-12px 0 0 21px}.legal-consent-container .hs-form-booleancheckbox-display input{float:left}.legal-consent-container .hs-form-booleancheckbox-display>span{display:block;margin-left:20px}.legal-consent-container .hs-form-booleancheckbox-display p{margin:0;display:inline}.legal-consent-container .hs-error-msgs label{color:#f2545b}.legal-consent-container~.hs_recaptcha{margin-top:18px}.cookie-reset-container{font-size:14px;margin-bottom:10px;text-align:right}#hs-outer-captcha-target,#hs-outer-captcha-target *{display:none;height:0;width:0}.hubspot-link__container{font-size:14px;padding-bottom:40px;position:relative;color:#9fa0a2;font-family:Helvetica Neue,Helvetica,Arial,sans-serif}.hubspot-link-text{color:#00a4bd;font-weight:400}.hubspot-link__container.sproket{color:#9fa0a2}.hubspot-link{color:#9fa0a2}.hubspot-link,.hubspot-link:hover{text-decoration:none}.hubspot-link:hover .hubspot-link-text{text-decoration:underline}.hubspot-link__icon{margin-bottom:-1px;margin-right:5px}.hubspot-link__container.sproket .hubspot-link__icon{width:30px;margin-right:0;float:left;margin-top:-9px;margin-left:-5px}</style><script async="" src="https://www.googletagmanager.com/gtag/js?id=AW-770268826"></script><script type="text/javascript" referrerpolicy="no-referrer-when-downgrade" async="" src="https://app.hubspot.com/content-tools-menu/api/v1/tools-menu/landing-pages/103353042004/actions?portalId=8667013&amp;callback=jsonpHandler"></script><script src="https://app.hubspot.com/content/editor/prefetcher.js"></script><link rel="prefetch" href="https://static.hsappstatic.net/page-editor-ui/static-1.6684/bundles/project.js"><link rel="prefetch" href="https://static.hsappstatic.net/page-editor-ui/static-1.6684/sass/project.css"><link rel="prefetch" href="https://static.hsappstatic.net/InpageEditorUI/static-1.44975/bundles/app.js"><link rel="prefetch" href="https://static.hsappstatic.net/InpageEditorUI/static-1.44975/bundles/app.css"><link rel="prefetch" href="https://static.hsappstatic.net/head-dlb/static-1.270/bundle.production.js"></head>
  <body><style type="text/css">html.hs-messages-widget-open.hs-messages-mobile,html.hs-messages-widget-open.hs-messages-mobile body{overflow:hidden!important;position:relative!important}html.hs-messages-widget-open.hs-messages-mobile body{height:100%!important;margin:0!important}#hubspot-messages-iframe-container{display:initial!important;z-index:2147483647;position:fixed!important;bottom:0!important}#hubspot-messages-iframe-container.widget-align-left{left:0!important}#hubspot-messages-iframe-container.widget-align-right{right:0!important}#hubspot-messages-iframe-container.internal{z-index:1016}#hubspot-messages-iframe-container.internal iframe{min-width:108px}#hubspot-messages-iframe-container .shadow-container{display:initial!important;z-index:-1;position:absolute;width:0;height:0;bottom:0;content:""}#hubspot-messages-iframe-container .shadow-container.internal{display:none!important}#hubspot-messages-iframe-container .shadow-container.active{width:400px;height:400px}#hubspot-messages-iframe-container iframe{display:initial!important;width:100%!important;height:100%!important;border:none!important;position:absolute!important;bottom:0!important;right:0!important;background:transparent!important}</style>
<!--  Added by GoogleTagManager integration -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M3TVNDT" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<!-- /Added by GoogleTagManager integration -->

    <div class="body-wrapper   hs-content-id-103353042004 hs-site-page page  ">
      
        <div id="hs_cos_wrapper_page_settings" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module"><!-- custom widget definition not found (portalId: 8667013, path: @marketplace/maka_Agency/POWER THEME/modules/page-settings.module, moduleId: 66458235757) --></div> 
      

      
        <div data-global-resource-path="POWER x OCEANIO/templates/partials/header.html"><header class="header">

    
    <a href="#main-content" class="pwr-header__skip">Skip to content</a>

    <div class="header__container">
            <div id="hs_cos_wrapper_header_page" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    


















<div id="pwr-js-burger" class="pwr-burger pwr--light ">
  <a href="#" id="pwr-js-burger__trigger-close" class="pwr-burger__trigger-close">
    <span class="pwr-burger__icon-close"></span>Close
  </a>
  
      
          <div class="pwr-burger__menu pwr-js-menu pwr-scroll-shadow__wrapper pwr-scroll-shadow__wrapper--vert pwr-scroll-shadow__root pwr-scroll-shadow__root--vert">
          
            <span id="hs_cos_wrapper_header_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="menu"><div id="hs_menu_wrapper_header_page_" class="hs-menu-wrapper active-branch no-flyouts hs-menu-flow-vertical pwr-scroll-shadow__sensor pwr-scroll-shadow__sensor--vert" role="navigation" data-sitemap-name="default" data-menu-id="83537384456" aria-label="Navigation Menu">
 <ul role="menu">
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none"><a href="https://www.ocean.io/solutions" aria-haspopup="true" aria-expanded="false" role="menuitem">Solutions</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions" role="menuitem">Overview</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions-for-sales" role="menuitem">For Sales</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions-for-marketing" role="menuitem">For Marketing</a></li>
   </ul></li>
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/pricing" role="menuitem">Pricing</a></li>
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/our-data" role="menuitem">Our Data</a></li>
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/contact-us" role="menuitem">Contact</a></li>
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none"><a href="https://blog.ocean.io" aria-haspopup="true" aria-expanded="false" role="menuitem">Resources</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/about-us" role="menuitem">About Us</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/case-studies" role="menuitem">Case Studies</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://blog.ocean.io" role="menuitem">Blog</a></li>
   </ul></li>
 </ul>
</div></span>
          
          </div>
      
  
  <div class="pwr-burger-bottom-bar">
    
    
    
    <div class="pwr-burger-bottom-bar__item">
      <a href="#" id="pwr-js-burger-language__trigger" class="pwr-burger-bottom-bar__item-link pwr-burger-language__trigger">LANGUAGE – en</a>
      <div id="pwr-js-burger-language__inner" class="pwr-burger-bottom-bar__inner pwr-burger-language__inner hs-skip-lang-url-rewrite">
        
            
            <a class="pwr-burger-bottom-bar__item-link pwr-burger-language__link" lang="de" href="https://www.ocean.io/de/">de</a>
            
        
      </div>
    </div>
    
    
      
    <div class="pwr-burger-bottom-bar__item pwr-cta pwr-cta--regular-border  ">
      <a class="cta_button" href="https://app.ocean.io/?__hstc=260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&amp;__hssc=260949202.1.1677144740057&amp;__hsfp=1432596156&amp;hsutk=ebc3794741760a85fbef4b715729a749&amp;contentType=standard-page" rel="noopener" title="Button Login">Login</a>                    
    </div>            
    
    <!-- 2nd Button -->
      
    <div class="pwr-burger-bottom-bar__item pwr-cta pwr-cta--custom-01  ">
      <a class="cta_button" href="https://get.ocean.io/get-in-touch?hsLang=en&amp;__hstc=260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&amp;__hssc=260949202.1.1677144740057&amp;__hsfp=1432596156&amp;hsutk=ebc3794741760a85fbef4b715729a749&amp;contentType=standard-page" rel="noopener" title="Button Book Demo">Book Demo</a>                    
    </div>            
    
    </div>
</div>

<div id="pwr-header-fixed__spacer" class="pwr-header-fixed__spacer" style="height: 85px;"></div>

<div id="pwr-header-fixed" class="pwr-header pwr-header-fixed pwr--light pwr-header--light-on-scroll" style="top: 0px;">
  <div class="page-center pwr-header--padding">
    <div class="pwr-header-full pwr--clearfix">
      <div class="pwr-header-logo pwr-header-logo--has-sticky">
        
        
        
          
        
        
        
        <a href="//ocean.io?hsLang=en" aria-label="Back to Home"><img src="https://www.ocean.io/hubfs/Logo%20dark.svg" alt="Logo dark" class="pwr-header-logo__img" width="168" height="30"></a>
        
        
        <a href="//ocean.io?hsLang=en" aria-label="Back to Home"><img src="https://www.ocean.io/hubfs/Logo%20dark.svg" alt="Logo dark" class="pwr-header-logo__img--sticky" width="168" height="30"></a>
        
      </div>
      
      <div id="pwr-js-header__menu" class="pwr-header__menu pwr-header__menu--narrow-32  pwr-header__menu--dropdown ">
        
          
            <div class="pwr-js-menu">
              
                <span id="hs_cos_wrapper_header_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="menu"><div id="hs_menu_wrapper_header_page_" class="hs-menu-wrapper active-branch flyouts hs-menu-flow-horizontal" role="navigation" data-sitemap-name="default" data-menu-id="83537384456" aria-label="Navigation Menu">
 <ul role="menu">
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none"><a href="https://www.ocean.io/solutions" aria-haspopup="true" aria-expanded="false" role="menuitem">Solutions</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions" role="menuitem">Overview</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions-for-sales" role="menuitem">For Sales</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions-for-marketing" role="menuitem">For Marketing</a></li>
   </ul></li>
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/pricing" role="menuitem">Pricing</a></li>
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/our-data" role="menuitem">Our Data</a></li>
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/contact-us" role="menuitem">Contact</a></li>
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none"><a href="https://blog.ocean.io" aria-haspopup="true" aria-expanded="false" role="menuitem">Resources</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/about-us" role="menuitem">About Us</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/case-studies" role="menuitem">Case Studies</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://blog.ocean.io" role="menuitem">Blog</a></li>
   </ul></li>
 </ul>
</div></span>
              
            </div>
          
        </div>
      
      
      <div id="pwr-js-header-right-bar" class="pwr-header-right-bar ">
      
        
        
        
        <div class="pwr-header-right-bar__item pwr-header-right-bar__language-switcher">
        <a href="#" class="pwr-header-right-bar__link ">en</a>
          <div class="pwr-dropdown pwr-dropdown--language hs-skip-lang-url-rewrite">
            
                
                <a class="pwr-dropdown__link pwr-header-right-bar__language-link" lang="de" href="https://www.ocean.io/de/">de</a>
                
            
          </div>
        </div>
        
          
          <div class="pwr-header-right-bar__item pwr-header-right-bar__cta pwr-cta pwr-cta--regular-border  ">
            <a class="cta_button" href="https://app.ocean.io/?__hstc=260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&amp;__hssc=260949202.1.1677144740057&amp;__hsfp=1432596156&amp;hsutk=ebc3794741760a85fbef4b715729a749&amp;contentType=standard-page" rel="noopener" title="Button Login">Login</a>                    
          </div>     
        
        <!-- 2nd Button -->
          
          <div class="pwr-header-right-bar__item pwr-header-right-bar__cta pwr-header-right-bar__cta--second pwr-cta pwr-cta--custom-01  ">
            <a class="cta_button" href="https://get.ocean.io/get-in-touch?hsLang=en&amp;__hstc=260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&amp;__hssc=260949202.1.1677144740057&amp;__hsfp=1432596156&amp;hsutk=ebc3794741760a85fbef4b715729a749&amp;contentType=standard-page" rel="noopener" title="Button Book Demo">Book Demo</a>                    
          </div>     
        
      </div>
      
      <div id="pwr-js-header-search" class="pwr-header-search hs-search-field">
        <div class="pwr-header-search__inner">
          <div class="hs-search-field__bar"> 
            <form action="/hs-search-results" data-hs-cf-bound="true">
              <div class="pwr--relative">
                <input type="text" id="pwr-header-search__input" class="pwr-header-search__input hs-search-field__input" name="term" autocomplete="off" aria-label="Search" placeholder="Type search here. Hit enter to submit or escape to close.">
                <button class="pwr-search-field__icon" type="submit" aria-label="Search Button"><span id="hs_cos_wrapper_header_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" aria-hidden="true"><g id="search1_layer"><path d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"></path></g></svg></span></button>
                <a href="#" id="pwr-js-header-search__close" aria-label="Close Search" class="pwr-header-search__close">
                  <span class="pwr-header-search__close-icon"></span>
                </a>
              </div>
              <input type="hidden" name="limit" value="5">
                          
              
              
              
            </form>
          </div>
        </div>
      </div>
      <a href="#" id="pwr-js-burger__trigger-open" class="pwr-burger__trigger-open  pwr-burger__trigger-open--mobile-only">
        <div class="pwr-burger__icon-open">
          <span></span>
        </div>
      </a>
      
    </div>
  </div>
</div></div>
        </div>
</header></div>
      

      
<main id="main-content" class="body-container-wrapper">
    <div class="body-container">
        <div class="container-fluid">
<div class="row-fluid-wrapper">
<div class="row-fluid">
<div class="span12 widget-span widget-type-cell " style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-1 dnd-section dnd_area-row-0-padding dnd_area-row-0-background-image">
<div class="row-fluid ">
<div class="span7 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="7">

<div class="row-fluid-wrapper row-depth-1 row-number-2 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16667035161316" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-rich_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module"><span id="hs_cos_wrapper_module_16667035161316_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_rich_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="rich_text"><div data-widget-type="cell" data-x="0" data-w="12">
<h1 style="font-size: 4px;" data-widget-type="custom_widget" data-x="0" data-w="12" id="find-the-right-companies-and-right-people-at-the-right-time"><span style="color: #ffffff;">Find the right companies and right people at the right time</span></h1>
<div data-widget-type="custom_widget" data-x="0" data-w="12"><img src="https://www.ocean.io/hs-fs/hubfs/Group%20153142%20(1).png?width=656&amp;height=81&amp;name=Group%20153142%20(1).png" alt="Group 153142 (1)" width="656" height="81" loading="lazy" style="height: auto; max-width: 100%; width: 656px;" srcset="https://www.ocean.io/hs-fs/hubfs/Group%20153142%20(1).png?width=328&amp;height=41&amp;name=Group%20153142%20(1).png 328w, https://www.ocean.io/hs-fs/hubfs/Group%20153142%20(1).png?width=656&amp;height=81&amp;name=Group%20153142%20(1).png 656w, https://www.ocean.io/hs-fs/hubfs/Group%20153142%20(1).png?width=984&amp;height=122&amp;name=Group%20153142%20(1).png 984w, https://www.ocean.io/hs-fs/hubfs/Group%20153142%20(1).png?width=1312&amp;height=162&amp;name=Group%20153142%20(1).png 1312w, https://www.ocean.io/hs-fs/hubfs/Group%20153142%20(1).png?width=1640&amp;height=203&amp;name=Group%20153142%20(1).png 1640w, https://www.ocean.io/hs-fs/hubfs/Group%20153142%20(1).png?width=1968&amp;height=243&amp;name=Group%20153142%20(1).png 1968w" sizes="(max-width: 656px) 100vw, 656px"></div>
<div data-widget-type="custom_widget" data-x="0" data-w="12"><span style="font-size: 18px; font-weight: var(--fw-paragraph); letter-spacing: var(--ls-paragraph); background-color: transparent; font-family: var(--ff-text);">&nbsp;</span></div>
<div data-widget-type="custom_widget" data-x="0" data-w="12" style="line-height: 1.75;"><span style="font-size: 18px; font-weight: var(--fw-paragraph); letter-spacing: var(--ls-paragraph); background-color: transparent; font-family: var(--ff-text);">Traditional lead data providers generate messy lists and leave tons of perfect-fit businesses on the table. <span style="color: #3c55f5;"><strong>Grow your business efficiently</strong> </span>with lookalike search in Ocean.io's B2B prospecting data platform.</span></div>
<div data-widget-type="custom_widget" data-x="0" data-w="12"><span style="font-weight: normal;">&nbsp;</span></div>
</div></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-3 cell_16667035161312-row-1-vertical-alignment dnd-row">
<div class="row-fluid ">
<div class="span6 widget-span widget-type-cell cell_1666703527027-vertical-alignment cell_1666703527027-padding dnd-column" style="" data-widget-type="cell" data-x="0" data-w="6">

<div class="row-fluid-wrapper row-depth-1 row-number-4 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1673529900024" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-form" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
	



	<span id="hs_cos_wrapper_widget_1673529900024_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_form" style="" data-hs-cos-general-type="widget" data-hs-cos-type="form">
<div id="hs_form_target_widget_1673529900024" data-hs-forms-root="true"><form id="hsForm_3d12374d-4e1f-4753-8ee5-d74cf0c717b9_4284" method="POST" accept-charset="UTF-8" enctype="multipart/form-data" novalidate="" action="https://forms.hsforms.com/submissions/v3/public/submit/formsnext/multipart/8667013/3d12374d-4e1f-4753-8ee5-d74cf0c717b9" class="hs-form-private hsForm_3d12374d-4e1f-4753-8ee5-d74cf0c717b9 hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9 hs-form-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_0582b19b-1ca3-41fe-b1a2-609bc8628356 hs-form stacked hs-custom-form" target="target_iframe_3d12374d-4e1f-4753-8ee5-d74cf0c717b9_4284" data-instance-id="0582b19b-1ca3-41fe-b1a2-609bc8628356" data-form-id="3d12374d-4e1f-4753-8ee5-d74cf0c717b9" data-portal-id="8667013" data-hs-cf-bound="true"><div class="hs_email hs-email hs-fieldtype-text field hs-form-field"><label id="label-email-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_4284" class="" placeholder="Enter your Business Email" for="email-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_4284"><span>Business Email</span><span class="hs-form-required">*</span></label><legend class="hs-field-desc" style="display: none;"></legend><div class="input"><input id="email-3d12374d-4e1f-4753-8ee5-d74cf0c717b9_4284" name="email" required="" placeholder="" type="email" class="hs-input" inputmode="email" autocomplete="email" value=""></div></div><div class="hs_submit hs-submit"><div class="hs-field-desc" style="display: none;"></div><div class="actions"><input type="submit" class="hs-button primary large" value="Get a Free Trial"></div></div><input name="hs_context" type="hidden" value="{&quot;embedAtTimestamp&quot;:&quot;1677144739274&quot;,&quot;formDefinitionUpdatedAt&quot;:&quot;1674118644934&quot;,&quot;lang&quot;:&quot;en&quot;,&quot;userAgent&quot;:&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36&quot;,&quot;pageTitle&quot;:&quot;Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales&quot;,&quot;pageUrl&quot;:&quot;https://www.ocean.io/&quot;,&quot;pageId&quot;:&quot;103353042004&quot;,&quot;isHubSpotCmsGeneratedPage&quot;:true,&quot;canonicalUrl&quot;:&quot;https://www.ocean.io&quot;,&quot;contentType&quot;:&quot;standard-page&quot;,&quot;hutk&quot;:&quot;ebc3794741760a85fbef4b715729a749&quot;,&quot;__hsfp&quot;:1432596156,&quot;__hssc&quot;:&quot;260949202.1.1677144740057&quot;,&quot;__hstc&quot;:&quot;260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&quot;,&quot;formTarget&quot;:&quot;#hs_form_target_widget_1673529900024&quot;,&quot;formInstanceId&quot;:&quot;4284&quot;,&quot;abTestId&quot;:73193512021,&quot;pageName&quot;:&quot;Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales&quot;,&quot;locale&quot;:&quot;en&quot;,&quot;timestamp&quot;:1677144740067,&quot;originalEmbedContext&quot;:{&quot;portalId&quot;:&quot;8667013&quot;,&quot;formId&quot;:&quot;3d12374d-4e1f-4753-8ee5-d74cf0c717b9&quot;,&quot;region&quot;:&quot;na1&quot;,&quot;target&quot;:&quot;#hs_form_target_widget_1673529900024&quot;,&quot;isBuilder&quot;:false,&quot;isTestPage&quot;:false,&quot;formInstanceId&quot;:&quot;4284&quot;,&quot;formsBaseUrl&quot;:&quot;/_hcms/forms&quot;,&quot;css&quot;:&quot;&quot;,&quot;redirectUrl&quot;:&quot;https://get.ocean.io/free-trial-signup-st2&quot;,&quot;isMobileResponsive&quot;:true,&quot;abTestId&quot;:73193512021,&quot;pageName&quot;:&quot;Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales&quot;,&quot;pageId&quot;:&quot;103353042004&quot;,&quot;contentType&quot;:&quot;standard-page&quot;,&quot;formData&quot;:{&quot;cssClass&quot;:&quot;hs-form stacked hs-custom-form&quot;},&quot;isCMSModuleEmbed&quot;:true},&quot;correlationId&quot;:&quot;0582b19b-1ca3-41fe-b1a2-609bc8628356&quot;,&quot;renderedFieldsIds&quot;:[&quot;email&quot;],&quot;captchaStatus&quot;:&quot;NOT_APPLICABLE&quot;,&quot;emailResubscribeStatus&quot;:&quot;NOT_APPLICABLE&quot;,&quot;isInsideCrossOriginFrame&quot;:false,&quot;source&quot;:&quot;forms-embed-1.2730&quot;,&quot;sourceName&quot;:&quot;forms-embed&quot;,&quot;sourceVersion&quot;:&quot;1.2730&quot;,&quot;sourceVersionMajor&quot;:&quot;1&quot;,&quot;sourceVersionMinor&quot;:&quot;2730&quot;,&quot;_debug_allPageIds&quot;:{&quot;embedContextPageId&quot;:&quot;103353042004&quot;,&quot;analyticsPageId&quot;:&quot;103353042004&quot;,&quot;pageContextPageId&quot;:&quot;103353042004&quot;},&quot;_debug_embedLogLines&quot;:[{&quot;clientTimestamp&quot;:1677144739295,&quot;level&quot;:&quot;INFO&quot;,&quot;message&quot;:&quot;Retrieved customer callbacks used on embed context: [\&quot;getExtraMetaDataBeforeSubmit\&quot;]&quot;},{&quot;clientTimestamp&quot;:1677144739297,&quot;level&quot;:&quot;INFO&quot;,&quot;message&quot;:&quot;Retrieved countryCode property from normalized embed definition response: \&quot;BE\&quot;&quot;},{&quot;clientTimestamp&quot;:1677144740064,&quot;level&quot;:&quot;INFO&quot;,&quot;message&quot;:&quot;Retrieved analytics values from API response which may be overriden by the embed context: {\&quot;hutk\&quot;:\&quot;ebc3794741760a85fbef4b715729a749\&quot;,\&quot;canonicalUrl\&quot;:\&quot;https://www.ocean.io\&quot;,\&quot;contentType\&quot;:\&quot;standard-page\&quot;,\&quot;pageId\&quot;:\&quot;103353042004\&quot;}&quot;}]}"><iframe name="target_iframe_3d12374d-4e1f-4753-8ee5-d74cf0c717b9_4284" style="display: none;"></iframe></form></div>








</span>
</div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
<div class="span6 widget-span widget-type-cell cell_1673897328388-vertical-alignment dnd-column" style="" data-widget-type="cell" data-x="6" data-w="6">

<div class="row-fluid-wrapper row-depth-1 row-number-5 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget module_16738973283883-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16738973283883" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">

<hr style="
  width: 1%;
  border: 0 none;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: rgba(0, 0, 0, 0.0);
  margin-left: auto;
  margin-right: auto;
  margin-top: 0;
  margin-bottom: 0;
"></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
<div class="span5 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="7" data-w="5">

<div class="row-fluid-wrapper row-depth-1 row-number-6 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget widget_1666703696264-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1666703696264" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">

<hr style="
  width: 1%;
  border: 0 none;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: rgba(0, 0, 0, 0.0);
  margin-left: auto;
  margin-right: auto;
  margin-top: 0;
  margin-bottom: 0;
"></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-7 dnd_area-row-1-padding dnd-section dnd_area-row-1-force-full-width-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-8 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16735444147957" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    
    

    
    

    
    
    






  
  
  








<div class="pwr-sec-stats  pwr--dark pwr--sec-padding-t-sm pwr--padding-b-0 lazyloaded" style="background-color: rgba(41, 48, 61, 1.0)">
  
  

  

    
    
    


   
  <div class="pwr-sec-stats__wrapper ">
    <div class="pwr-stats pwr-stats--centered pwr--neg-margin-lr-10 pwr--clearfix">
      
      <div class="pwr-stat" data-mh="116581194" style="height: 90.5px;">
        <span class="pwr-stat__number" style="visibility: visible;">+25</span><span class="pwr-stat__suffix">%</span>
      <span class="pwr-stat__title pwr-stat__title--normal">Lead conversion</span>
      </div>
      
      <div class="pwr-stat" data-mh="116581194" style="height: 90.5px;">
        <span class="pwr-stat__number" style="visibility: visible;">-22</span><span class="pwr-stat__suffix">%</span>
      <span class="pwr-stat__title pwr-stat__title--normal">Cost per MQL</span>
      </div>
      
      <div class="pwr-stat" data-mh="116581194" style="height: 90.5px;">
        <span class="pwr-stat__number" style="visibility: visible;">2</span><span class="pwr-stat__suffix">X</span>
      <span class="pwr-stat__title pwr-stat__title--normal">Demo Booking Rates</span>
      </div>
      
    </div>
  </div>
    
    
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-9 dnd_area-row-2-force-full-width-section dnd_area-row-2-padding dnd-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-10 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget widget_1646920243164-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1646920243164" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    
    

    
    

    
    
    












<div class="pwr-sec-clients  pwr--light pwr--sec-padding-t-md pwr--sec-padding-b-md lazyloaded">
  
  

  

    
    
    


  
  <div class="pwr-sec-clients__slider pwr-sec-clients__slider--top  pwr--relative" data-nr-elements="6" data-autoplay="false" data-autoplay-timeout="2000" data-nav-arrows="false" data-nav-bullets="false">

    
    
    <div class="pwr-owl owl-carousel owl-loaded owl-drag">
      
        
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
      
    <div class="owl-stage-outer"><div class="owl-stage" style="transform: translate3d(-1204px, 0px, 0px); transition: all 0s ease-in-out 0s; width: 4816px;"><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=300&amp;name=Frame%20153236.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=600&amp;name=Frame%20153236.png 600w" alt="Frame 153236" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=300&amp;name=Frame%20153236.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=600&amp;name=Frame%20153236.png 600w">
          </div></div><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=300&amp;name=Frame%20153234.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=600&amp;name=Frame%20153234.png 600w" alt="Frame 153234" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=300&amp;name=Frame%20153234.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=600&amp;name=Frame%20153234.png 600w">
          </div></div><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=300&amp;name=Frame%20153239.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=600&amp;name=Frame%20153239.png 600w" alt="Frame 153239" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=300&amp;name=Frame%20153239.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=600&amp;name=Frame%20153239.png 600w">
          </div></div><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=300&amp;name=Frame%20153238.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=600&amp;name=Frame%20153238.png 600w" alt="Frame 153238" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=300&amp;name=Frame%20153238.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=600&amp;name=Frame%20153238.png 600w">
          </div></div><div class="owl-item active" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=300&amp;name=Frame%20153233.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=600&amp;name=Frame%20153233.png 600w" alt="Frame 153233" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=300&amp;name=Frame%20153233.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=600&amp;name=Frame%20153233.png 600w">
          </div></div><div class="owl-item active" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=300&amp;name=Frame%20153237.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=600&amp;name=Frame%20153237.png 600w" alt="Frame 153237" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=300&amp;name=Frame%20153237.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=600&amp;name=Frame%20153237.png 600w">
          </div></div><div class="owl-item" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=300&amp;name=Frame%20153235.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=600&amp;name=Frame%20153235.png 600w" alt="Frame 153235" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=300&amp;name=Frame%20153235.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=600&amp;name=Frame%20153235.png 600w">
          </div></div><div class="owl-item" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=300&amp;name=Frame%20153240.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=600&amp;name=Frame%20153240.png 600w" alt="Frame 153240" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=300&amp;name=Frame%20153240.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=600&amp;name=Frame%20153240.png 600w">
          </div></div><div class="owl-item" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=300&amp;name=Frame%20153236.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=600&amp;name=Frame%20153236.png 600w" alt="Frame 153236" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=300&amp;name=Frame%20153236.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153236.png?width=600&amp;name=Frame%20153236.png 600w">
          </div></div><div class="owl-item" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=300&amp;name=Frame%20153234.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=600&amp;name=Frame%20153234.png 600w" alt="Frame 153234" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=300&amp;name=Frame%20153234.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153234.png?width=600&amp;name=Frame%20153234.png 600w">
          </div></div><div class="owl-item" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=300&amp;name=Frame%20153239.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=600&amp;name=Frame%20153239.png 600w" alt="Frame 153239" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=300&amp;name=Frame%20153239.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153239.png?width=600&amp;name=Frame%20153239.png 600w">
          </div></div><div class="owl-item" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=300&amp;name=Frame%20153238.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=600&amp;name=Frame%20153238.png 600w" alt="Frame 153238" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=300&amp;name=Frame%20153238.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153238.png?width=600&amp;name=Frame%20153238.png 600w">
          </div></div><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=300&amp;name=Frame%20153233.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=600&amp;name=Frame%20153233.png 600w" alt="Frame 153233" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=300&amp;name=Frame%20153233.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153233.png?width=600&amp;name=Frame%20153233.png 600w">
          </div></div><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=300&amp;name=Frame%20153237.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=600&amp;name=Frame%20153237.png 600w" alt="Frame 153237" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=300&amp;name=Frame%20153237.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153237.png?width=600&amp;name=Frame%20153237.png 600w">
          </div></div><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=300&amp;name=Frame%20153235.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=600&amp;name=Frame%20153235.png 600w" alt="Frame 153235" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=300&amp;name=Frame%20153235.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153235.png?width=600&amp;name=Frame%20153235.png 600w">
          </div></div><div class="owl-item cloned" style="width: 301px;"><div class="item pwr-sec-clients__logo ">
            <img data-srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=300&amp;name=Frame%20153240.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=600&amp;name=Frame%20153240.png 600w" alt="Frame 153240" class="pwr-sec-clients__logo-img ls-is-cached lazyloaded" width="200" srcset="https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=300&amp;name=Frame%20153240.png 300w, https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20153240.png?width=600&amp;name=Frame%20153240.png 600w">
          </div></div></div></div><div class="owl-nav disabled"><button type="button" role="presentation" class="owl-prev"><span aria-label="Previous">‹</span></button><button type="button" role="presentation" class="owl-next"><span aria-label="Next">›</span></button></div><div class="owl-dots disabled"></div></div>
    <div class="pwr-owl-nav pwr--disabled">
      <span class="pwr-owl-nav__prev pwr-icon">
        <svg version="1.1" id="arrow_left" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15 25" xml:space="preserve">
          <polygon points="12,24.7 0,12.3 12,0 13.4,1.4 2.8,12.3 13.4,23.3 "></polygon>
        </svg>
      </span>
      <span class="pwr-owl-nav__next pwr-icon">
        <svg version="1.1" id="arrow_right" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15 25" xml:space="preserve">
          <polygon points="1.4,24.7 13.4,12.3 1.4,0 0,1.4 10.6,12.3 0,23.3 "></polygon>
        </svg>
      </span>            
    </div>

    
    

  </div>
    
    
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-11 dnd-section dnd_area-row-3-padding dnd_area-row-3-background-color dnd_area-row-3-force-full-width-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-12 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1647029044259" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







  
  
  






    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col pwr--align-c pwr--light pwr--sec-padding-t-md pwr--padding-b-0 lazyloaded" style="background-color: rgba(244, 246, 249, 1.0)">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
       
      
      <h2 class="pwr-sec__title pwr-sec__title--default  pwr-sec-txt__title" id="how-is-ocean.io-different-from-other-b2b-data-providers">How is <a href="https://www.ocean.io/demo?hsLang=en">Ocean.io</a> different from other B2B data providers?</h2>
      
    </div>
    
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-13 dnd-section dnd_area-row-4-background-color dnd_area-row-4-padding">
<div class="row-fluid ">
<div class="span6 widget-span widget-type-cell cell_16680830389655-padding dnd-column" style="" data-widget-type="cell" data-x="0" data-w="6">

<div class="row-fluid-wrapper row-depth-1 row-number-14 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16680830389662" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







  
  
  






    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col  pwr--light pwr--padding-t-0 pwr--padding-b-0 lazyloaded" style="background-color: rgba(244, 246, 249, 1.0)">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
       
      
      <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="ai-lookalike-search">AI lookalike search</h3>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <p>Type in the URLs of a few companies you've sold to, and Ocean.io crawls the internet to find every company that describes themselves in the same way.</p>
<p>You'll be surprised how many companies you've been missing out on due to the (sometimes) arbitrary industry codes they're assigned in other databases.&nbsp;</p>
<p>&nbsp;</p>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
<div class="span6 widget-span widget-type-cell cell_1675779264919-padding dnd-column" style="" data-widget-type="cell" data-x="6" data-w="6">

<div class="row-fluid-wrapper row-depth-1 row-number-15 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16757792649193" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







  
  
  






    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col  pwr--light pwr--padding-t-0 pwr--padding-b-0 lazyloaded" style="background-color: rgba(244, 246, 249, 1.0)">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
       
      
      <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="company-first-approach">Company-first approach</h3>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <p><span style="color: #3c55f5;"><span style="color: #000000;">Ocean.io finds great-fit companies first,</span></span> and then finds people once you've set your account list, so you'll never miss out on an account due to a mismatching job title again.</p>
<p>Other platforms search for "[job title] in [industry]", which means you'll miss every company that doesn't have that specific job title (or every company where their database is missing that particular contact!)</p>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-16 dnd-section dnd_area-row-5-padding">
<div class="row-fluid ">
<div class="span5 widget-span widget-type-cell cell_16680830535405-padding dnd-column" style="" data-widget-type="cell" data-x="0" data-w="5">

<div class="row-fluid-wrapper row-depth-1 row-number-17 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16680830535408" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    











    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col  pwr--light pwr--padding-t-0 pwr--padding-b-0 lazyloaded">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
      
      <span class="pwr-sec__title-intro pwr-sec__title-intro--left pwr-sec__title-intro--narrow pwr-sec-txt__title-intro">
        AI Lookalikes
      </span>
       
      
      <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="target-niches-no-other-data-provider-can">Target niches no other data provider can</h3>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <div>
<div>
<div>
<p style="line-height: 1.75;">Lookalike search goes lightyears beyond the simple search filters of the past to bring you exactly what you're looking for. Want Subscription-based eCommerce companies? Drone software makers? Hydraulics manufacturers? We've got you covered.</p>
</div>
</div>
</div>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-18 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget widget_1673860988459-flexbox-positioning dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1673860988459" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
    






  



<span id="hs_cos_wrapper_widget_1673860988459_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked_image"><img src="https://www.ocean.io/hubfs/capterra.svg" class="hs-image-widget " style="max-width: 100%; height: auto;" alt="capterra" title="capterra" loading="lazy"></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
<div class="span7 widget-span widget-type-cell dnd-column cell_16680830535406-padding" style="" data-widget-type="cell" data-x="5" data-w="7">

<div class="row-fluid-wrapper row-depth-1 row-number-19 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget module_1668083053541-flexbox-positioning dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_1668083053541" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
    






  



<span id="hs_cos_wrapper_module_1668083053541_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked_image"><img src="https://www.ocean.io/hubfs/Frame%20153853%20(1).png" class="hs-image-widget " style="max-width: 100%; height: auto;" alt="Frame 153853 (1)" title="Frame 153853 (1)" loading="lazy"></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-20 dnd_area-row-6-padding dnd-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-21 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_1660040339519" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    











    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col pwr--align-c pwr--light pwr--sec-padding-t-sm pwr--padding-b-0 lazyload">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
       
      
      <h2 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="context-matters">Context matters</h2>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <p style="line-height: 1.75;">Ocean.io reads all the text on a website, not just keywords, in order to find lookalikes.<br>When building target accounts at scale, subtle changes make big differences in list accuracy.</p>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-22 dnd-section dnd_area-row-7-padding">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-23 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget module_16600405384383-flexbox-positioning dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16600405384383" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
    






  



<span id="hs_cos_wrapper_module_16600405384383_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked_image"><img src="https://www.ocean.io/hubfs/Frame%20153857%20(1).png" class="hs-image-widget " style="max-width: 100%; height: auto;" alt="Frame 153857 (1)" title="Frame 153857 (1)" loading="lazy"></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-24 dnd-section dnd_area-row-8-padding dnd_area-row-8-background-color">
<div class="row-fluid ">
<div class="span5 widget-span widget-type-cell cell_16680830915296-padding dnd-column" style="" data-widget-type="cell" data-x="0" data-w="5">

<div class="row-fluid-wrapper row-depth-1 row-number-25 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16680830915299" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







  
  
  






    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col  pwr--light pwr--padding-t-0 pwr--padding-b-0 lazyload" style="background-color: rgba(244, 246, 249, 1.0)">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
      
      <span class="pwr-sec__title-intro pwr-sec__title-intro--left pwr-sec__title-intro--narrow pwr-sec-txt__title-intro">
        Search filters
      </span>
       
      
      <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="unrivalled-filtering-options">Unrivalled filtering options</h3>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <div>
<div>
<div data-widget-type="cell" data-x="7" data-w="5">
<div>
<div>
<div data-widget-type="custom_widget" data-x="0" data-w="12">
<div>
<div>
<div>
<div>
<p>Dial in your targeting to the exact profile you're looking for with powerful filtering options. Ocean.io offers several filters you won't find anywhere else, thanks to the fact that the dataset is sourced via web crawlers.</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
<div class="span7 widget-span widget-type-cell dnd-column cell_16680830915297-padding" style="" data-widget-type="cell" data-x="5" data-w="7">

<div class="row-fluid-wrapper row-depth-1 row-number-26 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget module_1668083091530-flexbox-positioning dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_1668083091530" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
    






  



<span id="hs_cos_wrapper_module_1668083091530_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked_image"><img src="https://www.ocean.io/hubfs/Filters%20Image(1).png" class="hs-image-widget " style="max-width: 100%; height: auto;" alt="Filters Image(1)" title="Filters Image(1)" loading="lazy"></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-27 dnd-section dnd_area-row-9-padding">
<div class="row-fluid ">
<div class="span7 widget-span widget-type-cell cell_16680830728226-padding dnd-column" style="" data-widget-type="cell" data-x="0" data-w="7">

<div class="row-fluid-wrapper row-depth-1 row-number-28 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget module_1668083072823-flexbox-positioning dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_1668083072823" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
    






  



<span id="hs_cos_wrapper_module_1668083072823_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked_image"><img src="https://www.ocean.io/hubfs/Frame%20153900.png" class="hs-image-widget " style="max-width: 100%; height: auto;" alt="Frame 153900" title="Frame 153900" loading="lazy"></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
<div class="span5 widget-span widget-type-cell dnd-column cell_16680830728227-padding" style="" data-widget-type="cell" data-x="7" data-w="5">

<div class="row-fluid-wrapper row-depth-1 row-number-29 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16680830728233" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    











    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col  pwr--light pwr--padding-t-0 pwr--padding-b-0 lazyload">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
      
      <span class="pwr-sec__title-intro pwr-sec__title-intro--left pwr-sec__title-intro--narrow pwr-sec-txt__title-intro">
        CRM Integration
      </span>
       
      
      <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="build-better-qualified-pipeline">Build better qualified pipeline</h3>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <div>
<div>
<div>
<p style="line-height: 1.75;">Ocean.io builds lead lists based on your actual sales performance, and continuously updates and optimizes recommendations as you close new business.</p>
</div>
</div>
</div>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-30 dnd-section dnd_area-row-10-background-color dnd_area-row-10-padding">
<div class="row-fluid ">
<div class="span5 widget-span widget-type-cell cell_16768900970692-padding dnd-column" style="" data-widget-type="cell" data-x="0" data-w="5">

<div class="row-fluid-wrapper row-depth-1 row-number-31 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_1676890097071" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







  
  
  






    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col  pwr--light pwr--padding-t-0 pwr--padding-b-0 lazyload" style="background-color: rgba(244, 246, 249, 1.0)">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
      
      <span class="pwr-sec__title-intro pwr-sec__title-intro--left pwr-sec__title-intro--narrow pwr-sec-txt__title-intro">
        Targeting
      </span>
       
      
      <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="boost-your-sales-and-marketing-efficiency">Boost your Sales and Marketing Efficiency</h3>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <div>
<div>
<div>
<p style="line-height: 1.75;">More accurate lists and tighter targeting have knock-on effects for your whole Sales and Marketing engines: Better personalization, higher conversion rates, and less wasted spend and effort.</p>
</div>
</div>
</div>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
<div class="span7 widget-span widget-type-cell dnd-column cell_16768900970693-padding" style="" data-widget-type="cell" data-x="5" data-w="7">

<div class="row-fluid-wrapper row-depth-1 row-number-32 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget module_16768900970713-flexbox-positioning dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16768900970713" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
    






  



<span id="hs_cos_wrapper_module_16768900970713_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_linked_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked_image"><img src="https://www.ocean.io/hubfs/Frame%20153899%20(1).png" class="hs-image-widget " style="max-width: 100%; height: auto;" alt="Frame 153899 (1)" title="Frame 153899 (1)" loading="lazy"></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-33 dnd-section dnd_area-row-11-padding">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-34 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16600401410304" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    











    
    

    
    

    
    
    





<div class="pwr-sec-txt pwr-sec-txt--1col pwr--align-c pwr--light pwr--sec-padding-t-md pwr--padding-b-0 lazyload">
  
  

  

    
    
    

  
  <div class="page-center pwr--relative pwr--clearfix">
    
    <div class="pwr-sec-txt__intro-sec">
       
      
      <h2 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-txt__title" id="more-effective-outreach-via-precise-vertical-targeting.">More effective outreach via precise vertical targeting.</h2>
      
    </div>
    
    
    <div class="pwr-sec-txt__content pwr-sec-txt__content--top  pwr--clearfix">
        <div class="pwr-rich-text pwr-sec-txt__left">
          <p style="line-height: 1.75;">Ocean.io crawls the internet to categorize companies by what they&nbsp;<span style="background-color: #3c55f5; color: #ffffff;"> actually do&nbsp;</span> instead of using generic industry categories.<br>When your targeting is airtight you can create truly relevant messaging, efficient ad spend, and smashed targets.</p>
        </div>
        
      </div>
    
  </div>
  
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-35 dnd_area-row-12-padding dnd-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-36 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1663927128610" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module widget-type-rich_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module"><span id="hs_cos_wrapper_widget_1663927128610_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_rich_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="rich_text"><h3 style="line-height: 1.75; text-align: center;" id="how-ocean.io-lookalike-search-works">How Ocean.io Lookalike Search Works</h3></span></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-37 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1663926010817" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
  
    
      
      
      <div class="hs-video-widget" data-hsv-embed-id="1650d674-634b-4d47-b82d-94fa2ae194f2" data-hsv-status="rendered">
  <img src="https://api-na1.hubapi.com/video/v1/public/83983727772/poster?portalId=8667013" style="max-width: 600px; display: none !important;" alt="HubSpot Video" data-hsv-id="83983727772" data-hsv-play-button-color="#ffffff" data-hsv-width="600" data-hsv-height="426" data-hsv-autoplay="true" data-hsv-loop="true" data-hsv-hidden-controls="true" data-hsv-full-width="false">
<div class="hs-video-container" style="max-width: 600px;   margin: 0 auto">
      <div class="hs-video-wrapper" style="position: relative; height: 0; padding-bottom: 71%;">
        <iframe id="hs_player_1650d674-634b-4d47-b82d-94fa2ae194f2" src="https://play.hubspotvideo.com/v/8667013/id/83983727772?autoplay=true&amp;loop=true&amp;hiddenControls=true&amp;renderContext=onload-placeholder&amp;parentOrigin=https%3A%2F%2Fwww.ocean.io&amp;pageId=103353042004&amp;locale=en#hsvid=1650d674-634b-4d47-b82d-94fa2ae194f2&amp;t=1677144739080" loading="lazy" referrerpolicy="origin" sandbox="allow-forms allow-scripts allow-same-origin allow-popups" allow="autoplay; fullscreen;" style="position: absolute !important; width: 100% !important; height: 100% !important; left: 0; top: 0; border: 0 none; pointer-events: initial; ">
        </iframe>
      </div>
    </div></div>

    
  


</div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-38 dnd_area-row-13-padding dnd-section dnd_area-row-13-force-full-width-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-39 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd_area-module-6-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_dnd_area-module-6" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    
    

    
    

    
    
    




  
  
  






<div class="pwr-sec-testimonials  pwr--dark pwr--sec-padding-t-md pwr--sec-padding-b-md lazyload" style="background-color: rgba(60, 85, 245, 1.0)">
  
  

  

    
    
    


  <div class="page-center pwr--relative">
    
  </div>


    
  <div class="page-center pwr--relative">
    <div class="pwr-sec-testimonials__slider pwr--relative" data-autoplay="true" data-autoplay-timeout="15000" data-nav-arrows="true" data-nav-bullets="false">
      <div class="pwr-owl owl-carousel owl-loaded owl-drag">
        
          
        
          
        
          
        
          
        
      <div class="owl-stage-outer owl-height" style="height: 293px;"><div class="owl-stage" style="transform: translate3d(-2488px, 0px, 0px); transition: all 0.4s ease-in-out 0s; width: 4976px;"><div class="owl-item cloned" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote">“<span>Today we can more confidently say we're reaching out to all the companies that could potentially buy from us</span><span>."</span></div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/People%20Photos%20-%20Case%20Studies/Josh%20Pudnos.jpeg" alt="Josh Pudnos" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Josh Pudnos</span>
                
                <span class="pwr-testimonial__job-title">Brandwatch</span>
                
              </div>
            </div>
                        
          </div></div><div class="owl-item cloned" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote">" I feel like Neo seeing numbers in the matrix! Show me niches, lots of niches!"&nbsp;</div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/Preetum%20Mistry-1.jpeg" alt="Preetum Mistry-1" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Preetum Mistry</span>
                
                <span class="pwr-testimonial__job-title">Co-Founder @ DigiPly Media </span>
                
              </div>
            </div>
                        
          </div></div><div class="owl-item" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote"><span>”We doubled our demo booking rate in the first week."</span></div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/Quirijn_Leadinfo-1.png" alt="Quirijn_Leadinfo-1" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Quirjin Kleppe</span>
                
                <span class="pwr-testimonial__job-title">Leadinfo</span>
                
              </div>
            </div>
                        
          </div></div><div class="owl-item" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote">“Our false positive rate was north of 30% building target account lists <span>using SIC, NACIS, D&amp;B’s or LinkedIn’s industry classifications, and with Ocean.io it's now under 3%.</span>”</div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/Erik%20Paulson%20Vendisys.jpeg" alt="Erik Paulson Vendisys" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Erik Paulson</span>
                
                <span class="pwr-testimonial__job-title">CEO @ Vendisys</span>
                
              </div>
            </div>
                        
          </div></div><div class="owl-item active" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote">“<span>Today we can more confidently say we're reaching out to all the companies that could potentially buy from us</span><span>."</span></div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/People%20Photos%20-%20Case%20Studies/Josh%20Pudnos.jpeg" alt="Josh Pudnos" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Josh Pudnos</span>
                
                <span class="pwr-testimonial__job-title">Brandwatch</span>
                
              </div>
            </div>
                        
          </div></div><div class="owl-item" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote">" I feel like Neo seeing numbers in the matrix! Show me niches, lots of niches!"&nbsp;</div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/Preetum%20Mistry-1.jpeg" alt="Preetum Mistry-1" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Preetum Mistry</span>
                
                <span class="pwr-testimonial__job-title">Co-Founder @ DigiPly Media </span>
                
              </div>
            </div>
                        
          </div></div><div class="owl-item cloned" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote"><span>”We doubled our demo booking rate in the first week."</span></div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/Quirijn_Leadinfo-1.png" alt="Quirijn_Leadinfo-1" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Quirjin Kleppe</span>
                
                <span class="pwr-testimonial__job-title">Leadinfo</span>
                
              </div>
            </div>
                        
          </div></div><div class="owl-item cloned" style="width: 602px; margin-right: 20px;"><div class="pwr-testimonial pwr-testimonial--style-2">
            <div class="pwr-rich-text pwr-testimonial__quote">“Our false positive rate was north of 30% building target account lists <span>using SIC, NACIS, D&amp;B’s or LinkedIn’s industry classifications, and with Ocean.io it's now under 3%.</span>”</div>
            <div class="pwr-testimonial__author">
              
              <div class="pwr-avatar pwr-avatar--valign pwr-testimonial__avatar">
                <div class="pwr-avatar__round pwr-avatar__small">
                  <img class="pwr-avatar__img lazyload" data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/Erik%20Paulson%20Vendisys.jpeg" alt="Erik Paulson Vendisys" width="70" height="70">
                </div>
              </div>
              
              <div class="pwr-testimonial__info">
                <span class="pwr-testimonial__name pwr-testimonial__name--has-job-desc">Erik Paulson</span>
                
                <span class="pwr-testimonial__job-title">CEO @ Vendisys</span>
                
              </div>
            </div>
                        
          </div></div></div></div><div class="owl-nav disabled"><button type="button" role="presentation" class="owl-prev"><span aria-label="Previous">‹</span></button><button type="button" role="presentation" class="owl-next"><span aria-label="Next">›</span></button></div><div class="owl-dots disabled"></div></div>
      
      <div class="pwr-owl-nav">
        <span class="pwr-owl-nav__prev pwr-icon">
          <svg version="1.1" id="arrow_left" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15 25" xml:space="preserve">
          <polygon points="12,24.7 0,12.3 12,0 13.4,1.4 2.8,12.3 13.4,23.3 "></polygon>
          </svg>
        </span>
        <span class="pwr-owl-nav__next pwr-icon">
          <svg version="1.1" id="arrow_right" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15 25" xml:space="preserve">
            <polygon points="1.4,24.7 13.4,12.3 1.4,0 0,1.4 10.6,12.3 0,23.3 "></polygon>
          </svg>
        </span>            
      </div>
      
    </div> 
  </div>

  

  
    
    
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-40 dnd-section dnd_area-row-14-force-full-width-section dnd_area-row-14-padding">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-41 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16630828250404" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    



  
    
    
    
    

    
      
      
      

    

  






<div class="pwr-sec-cta pwr-sec-cta--cta-only pwr-sec-cta--primary pwr--sec-padding-t-lg pwr--sec-padding-b-lg lazyload " style="background-color: transparent;">
  
    <img data-src="https://8667013.fs1.hubspotusercontent-na1.net/hubfs/8667013/Frame%20153735.png" class="pwr-parallax lazyload" alt="Frame 153735" width="2000">
  
  

  
  <div class="pwr--abs-full" style="background-color: rgba(20, 20, 20, 0.1)"></div>
  

    
    
    


  <div class="page-center pwr--align-c pwr--relative">
    
      
      <div class="pwr-sec-cta__cta--center pwr-cta pwr-cta--custom-03  ">
        <span id="hs_cos_wrapper_module_16630828250404_name" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_cta" style="" data-hs-cos-general-type="widget" data-hs-cos-type="cta"><!--HubSpot Call-to-Action Code --><span class="hs-cta-wrapper" id="hs-cta-wrapper-6267880d-d478-4deb-b59b-3d216840c074"><span class="hs-cta-node hs-cta-6267880d-d478-4deb-b59b-3d216840c074" id="hs-cta-6267880d-d478-4deb-b59b-3d216840c074" style="visibility: visible;" data-hs-drop="true"><a id="cta_button_8667013_ab1f6d1b-bf99-4cbd-9993-d291c17726f4" class="cta_button " href="https://www.ocean.io/cs/c/?cta_guid=ab1f6d1b-bf99-4cbd-9993-d291c17726f4&amp;signature=AAH58kHfpNJVtqc2G7RtFCrxrdqDJv3GsQ&amp;pageId=103353042004&amp;placement_guid=6267880d-d478-4deb-b59b-3d216840c074&amp;click=52423a8f-1edd-4491-8eba-7bd8133ceb29&amp;hsutk=ebc3794741760a85fbef4b715729a749&amp;canon=https%3A%2F%2Fwww.ocean.io%2F&amp;portal_id=8667013&amp;redirect_url=APefjpEmWj2bZQq2yt8mDzwUuwghHjQdxhg3XcOPj-XAA4QdeSLXsQfXqktkDc5UJFmWjmFrbqtiHykVbux5pzeAkW5rqhkQUFFq8sss4fm27UPj0yZILLaLiZuEEEwuUkLeU7GSt4XBnrsWOcPRPNHDr1uc7jc_bFk6uAR43x2g2kiFtvoOlplkAVUjAmukCiOLVdHWp_wZIOn49ee1hAKD5BGzFRNukq2X7qjRMZObRBLDMlvAuS0&amp;__hstc=260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&amp;__hssc=260949202.1.1677144740057&amp;__hsfp=1432596156&amp;contentType=standard-page" style="" cta_dest_link="https://get.ocean.io/get-a-demo" title="Show me how it works"><span style="font-size: 18px; color: #141414;">Show me how it works</span></a></span><script charset="utf-8" src="/hs/cta/cta/current.js"></script><script type="text/javascript"> hbspt.cta._relativeUrls=true;hbspt.cta.load(8667013, '6267880d-d478-4deb-b59b-3d216840c074', {"useNewLoader":"true","region":"na1"}); </script></span><!-- end HubSpot Call-to-Action Code --></span>
      </div>
      
    
  </div>
    
    
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-42 dnd-section dnd_area-row-15-force-full-width-section dnd_area-row-15-padding">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16630607738162" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    
    

    
    

    
    
    




  
  
  








<div class="pwr-sec-form  pwr--dark pwr--sec-padding-t-md pwr--sec-padding-b-md lazyload" style="background-color: rgba(20, 20, 20, 1.0)">
  
  

  

    
    
    
        

            
            

                
                

                <div id="shape-divider_module_16630607738162-1" class="pwr-shape-divider__shape pwr-shape-divider__shape--top ">
                    

    
    

    
    
        
        
            
        

    
    
    

    
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1360 99" preserveAspectRatio="none" class="pwr-shape-divider__svg">
        
        <path fill="#FFFFFF" opacity="1.0" d="M0 0c0 55.228 44.772 100 100 100h1160c55.228 0 100-44.772 100-100v101H0V0z" fill-rule="evenodd"></path>
        
    </svg>



                </div>
            

                
                

                <div id="shape-divider_module_16630607738162-2" class="pwr-shape-divider__shape pwr-shape-divider__shape--bottom ">
                    

    
    

    
    
        
        
            
        

    
    
    

    
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1360 99" preserveAspectRatio="none" class="pwr-shape-divider__svg">
        
        <path fill="#FFFFFF" opacity="1.0" d="M0 0c0 55.228 44.772 100 100 100h1160c55.228 0 100-44.772 100-100v101H0V0z" fill-rule="evenodd"></path>
        
    </svg>



                </div>
            

            
            
            <div class="pwr-shape-divider__offset-wrapper"> 
        
        
    


  
  <div class="page-center pwr--relative">
    <div class="pwr-sec-form__content  pwr-sec-form__content--narrow pwr--margin-centered pwr--align-c">
      <div class="pwr-sec-form__intro-sec pwr-sec-form__intro-sec--vertical ">
        
                
        <h2 class="pwr-sec__title pwr-sec__title--default pwr-sec-form__title" id="see-what-we-can-do-for-you">See what we can do for you</h2>
        
        
        <span class="pwr-rich-text pwr-sec__desc pwr-sec-form__desc">
          <div><span>Get a demo to see how much better your leads could be.</span></div>
        </span>
                  
      </div>
      
      <div class="pwr-form pwr-button--outlined pwr-sec-form__form  pwr-cta--custom-04">
        
        <span id="hs_cos_wrapper_module_16630607738162_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_form" style="" data-hs-cos-general-type="widget" data-hs-cos-type="form">
<div id="hs_form_target_form_module_vert_4d0c3ccb-f001-471d-824b-0ba9c0f9b704" data-hs-forms-root="true"><form id="hsForm_4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" method="POST" accept-charset="UTF-8" enctype="multipart/form-data" novalidate="" action="https://forms.hsforms.com/submissions/v3/public/submit/formsnext/multipart/8667013/4d0c3ccb-f001-471d-824b-0ba9c0f9b704" class="hs-form-private hsForm_4d0c3ccb-f001-471d-824b-0ba9c0f9b704 hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704 hs-form-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_8ac54dc1-af29-4362-997b-23013ea28b9b hs-form stacked hs-custom-form" target="target_iframe_4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" data-instance-id="8ac54dc1-af29-4362-997b-23013ea28b9b" data-form-id="4d0c3ccb-f001-471d-824b-0ba9c0f9b704" data-portal-id="8667013" data-hs-cf-bound="true"><div class="hs_vollstndiger_name hs-vollstndiger_name hs-fieldtype-text field hs-form-field smart-field"><label id="label-vollstndiger_name-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" class="" placeholder="Enter your Full name" for="vollstndiger_name-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300"><span>Full name</span><span class="hs-form-required">*</span></label><legend class="hs-field-desc" style="display: none;"></legend><div class="input"><input id="vollstndiger_name-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" name="vollstndiger_name" required="" placeholder="Full name" type="text" class="hs-input" inputmode="text" value=""></div></div><div class="hs_email hs-email hs-fieldtype-text field hs-form-field smart-field"><label id="label-email-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" class="" placeholder="Enter your Work E-mail" for="email-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300"><span>Work E-mail</span><span class="hs-form-required">*</span></label><legend class="hs-field-desc" style="display: none;"></legend><div class="input"><input id="email-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" name="email" required="" placeholder="Business E-mail" type="email" class="hs-input" inputmode="email" autocomplete="email" value=""></div></div><div class="hs_jobtitle hs-jobtitle hs-fieldtype-text field hs-form-field smart-field"><label id="label-jobtitle-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" class="" placeholder="Enter your Job title" for="jobtitle-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300"><span>Job title</span><span class="hs-form-required">*</span></label><legend class="hs-field-desc" style="display: none;"></legend><div class="input"><input id="jobtitle-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" name="jobtitle" required="" placeholder="Job Title" type="text" class="hs-input" inputmode="text" autocomplete="organization-title" value=""></div></div><div class="hs_company hs-company hs-fieldtype-text field hs-form-field"><label id="label-company-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" class="" placeholder="Enter your Company name" for="company-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300"><span>Company name</span></label><legend class="hs-field-desc" style="display: none;"></legend><div class="input"><input id="company-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" name="company" placeholder="Company Name" type="text" class="hs-input" inputmode="text" autocomplete="organization" value=""></div></div><div class="hs_website hs-website hs-fieldtype-text field hs-form-field smart-field"><label id="label-website-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" class="" placeholder="Enter your Website URL" for="website-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300"><span>Website URL</span><span class="hs-form-required">*</span></label><legend class="hs-field-desc" style="display: none;"></legend><div class="input"><input id="website-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" name="website" required="" placeholder="Website URL" type="text" class="hs-input" inputmode="url" value=""></div></div><div class="hs_phone hs-phone hs-fieldtype-phonenumber field hs-form-field smart-field"><label id="label-phone-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" class="" placeholder="Enter your Phone Number" for="phone-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300"><span>Phone Number</span><span class="hs-form-required">*</span></label><legend class="hs-field-desc" style="display: none;"></legend><div class="input"><input id="phone-4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" name="phone" required="" placeholder="Phone number" type="tel" class="hs-input" inputmode="tel" autocomplete="tel" value=""></div></div><div class="hs_submit hs-submit"><div class="hs-field-desc" style="display: none;"></div><div class="actions"><input type="submit" class="hs-button primary large" value="Get a demo"></div></div><input name="hs_context" type="hidden" value="{&quot;embedAtTimestamp&quot;:&quot;1677144739291&quot;,&quot;formDefinitionUpdatedAt&quot;:&quot;1675687196481&quot;,&quot;lang&quot;:&quot;en&quot;,&quot;embedType&quot;:&quot;SHARABLE&quot;,&quot;notifyHubSpotOwner&quot;:&quot;true&quot;,&quot;userAgent&quot;:&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36&quot;,&quot;pageTitle&quot;:&quot;Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales&quot;,&quot;pageUrl&quot;:&quot;https://www.ocean.io/&quot;,&quot;pageId&quot;:&quot;103353042004&quot;,&quot;isHubSpotCmsGeneratedPage&quot;:true,&quot;canonicalUrl&quot;:&quot;https://www.ocean.io&quot;,&quot;contentType&quot;:&quot;standard-page&quot;,&quot;hutk&quot;:&quot;ebc3794741760a85fbef4b715729a749&quot;,&quot;__hsfp&quot;:1432596156,&quot;__hssc&quot;:&quot;260949202.1.1677144740057&quot;,&quot;__hstc&quot;:&quot;260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&quot;,&quot;formTarget&quot;:&quot;#hs_form_target_form_module_vert_4d0c3ccb-f001-471d-824b-0ba9c0f9b704&quot;,&quot;formInstanceId&quot;:&quot;9300&quot;,&quot;abTestId&quot;:73193512021,&quot;pageName&quot;:&quot;Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales&quot;,&quot;locale&quot;:&quot;en&quot;,&quot;timestamp&quot;:1677144740071,&quot;originalEmbedContext&quot;:{&quot;portalId&quot;:&quot;8667013&quot;,&quot;formId&quot;:&quot;4d0c3ccb-f001-471d-824b-0ba9c0f9b704&quot;,&quot;region&quot;:&quot;na1&quot;,&quot;target&quot;:&quot;#hs_form_target_form_module_vert_4d0c3ccb-f001-471d-824b-0ba9c0f9b704&quot;,&quot;isBuilder&quot;:false,&quot;isTestPage&quot;:false,&quot;formInstanceId&quot;:&quot;9300&quot;,&quot;formsBaseUrl&quot;:&quot;/_hcms/forms&quot;,&quot;css&quot;:&quot;&quot;,&quot;redirectUrl&quot;:&quot;https://www.ocean.io/thank-you&quot;,&quot;isMobileResponsive&quot;:true,&quot;abTestId&quot;:73193512021,&quot;pageName&quot;:&quot;Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales&quot;,&quot;pageId&quot;:&quot;103353042004&quot;,&quot;contentType&quot;:&quot;standard-page&quot;,&quot;formData&quot;:{&quot;cssClass&quot;:&quot;hs-form stacked hs-custom-form&quot;},&quot;isCMSModuleEmbed&quot;:true},&quot;correlationId&quot;:&quot;8ac54dc1-af29-4362-997b-23013ea28b9b&quot;,&quot;renderedFieldsIds&quot;:[&quot;vollstndiger_name&quot;,&quot;email&quot;,&quot;jobtitle&quot;,&quot;company&quot;,&quot;website&quot;,&quot;phone&quot;],&quot;captchaStatus&quot;:&quot;NOT_APPLICABLE&quot;,&quot;emailResubscribeStatus&quot;:&quot;NOT_APPLICABLE&quot;,&quot;isInsideCrossOriginFrame&quot;:false,&quot;source&quot;:&quot;forms-embed-1.2730&quot;,&quot;sourceName&quot;:&quot;forms-embed&quot;,&quot;sourceVersion&quot;:&quot;1.2730&quot;,&quot;sourceVersionMajor&quot;:&quot;1&quot;,&quot;sourceVersionMinor&quot;:&quot;2730&quot;,&quot;_debug_allPageIds&quot;:{&quot;embedContextPageId&quot;:&quot;103353042004&quot;,&quot;analyticsPageId&quot;:&quot;103353042004&quot;,&quot;pageContextPageId&quot;:&quot;103353042004&quot;},&quot;_debug_embedLogLines&quot;:[{&quot;clientTimestamp&quot;:1677144739366,&quot;level&quot;:&quot;INFO&quot;,&quot;message&quot;:&quot;Retrieved customer callbacks used on embed context: [\&quot;getExtraMetaDataBeforeSubmit\&quot;]&quot;},{&quot;clientTimestamp&quot;:1677144739367,&quot;level&quot;:&quot;INFO&quot;,&quot;message&quot;:&quot;Retrieved countryCode property from normalized embed definition response: \&quot;BE\&quot;&quot;},{&quot;clientTimestamp&quot;:1677144740069,&quot;level&quot;:&quot;INFO&quot;,&quot;message&quot;:&quot;Retrieved analytics values from API response which may be overriden by the embed context: {\&quot;hutk\&quot;:\&quot;ebc3794741760a85fbef4b715729a749\&quot;,\&quot;canonicalUrl\&quot;:\&quot;https://www.ocean.io\&quot;,\&quot;contentType\&quot;:\&quot;standard-page\&quot;,\&quot;pageId\&quot;:\&quot;103353042004\&quot;}&quot;}]}"><iframe name="target_iframe_4d0c3ccb-f001-471d-824b-0ba9c0f9b704_9300" style="display: none;"></iframe></form></div>








</span>
        
      </div>
      
    </div>
  </div>
    
    
    
        
         
            </div> 
        
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-43 dnd_area-row-16-padding dnd-section dnd_area-row-16-force-full-width-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-44 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget widget_1647420016351-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1647420016351" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    
    

    
    

    
    
    




  
  
  










<div class="pwr-sec-mockup  pwr--light pwr--padding-t-0   lazyload" style="background-color: rgba(255, 255, 255, 1.0)">
  
  

  

    
    
    


  <div class="pwr-sec-mockup__content--pos-vert">
    <div class="page-center">
      <div class="pwr-sec-mockup__content " style="width: 40%;left: 60%;">
        
        
        <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec-mockup__title" id="segmentation-ai">Segmentation AI</h3>
        
        
        <span class="pwr-rich-text pwr-sec__desc pwr-sec-mockup__desc">
        <div>
<div><span data-aos="fade-in" data-aos-delay="50">Predict future revenue from various industries, countries, and regions.</span></div>
<div><span data-aos="fade-in" data-aos-delay="50">&nbsp;</span></div>
<div><span data-aos="fade-in" data-aos-delay="50">&nbsp;</span></div>
<div><span data-aos="fade-in" data-aos-delay="50">&nbsp;</span></div>
</div></span>
        
        
        
      </div>
    </div>
  </div>
  
  <div class=" pwr--relative pwr--clearfix">
    <div class="pwr-sec-mockup__mockup pwr-sec-mockup__mockup--desktop-align-default pwr-sec-mockup__mockup--mobile-align-default  " style="width: 45vw;max-width: 950px;">
      <div class="pwr-ratio-box" style="padding-bottom: calc(0.9384164222873901 * 100%);">
      <img data-srcset="
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/Untitled-1-3.png?width=288&amp;name=Untitled-1-3.png 288w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/Untitled-1-3.png?width=384&amp;name=Untitled-1-3.png 384w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/Untitled-1-3.png?width=496&amp;name=Untitled-1-3.png 496w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/Untitled-1-3.png?width=600&amp;name=Untitled-1-3.png 600w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/Untitled-1-3.png?width=1199&amp;name=Untitled-1-3.png 1199w" alt="Untitled-1-3" class="pwr-sec-mockup__mockup-img lazyload" width="1705">
        </div>
    </div> 
  </div>
  
    
    
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-45 dnd_area-row-17-padding dnd_area-row-17-force-full-width-section dnd-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-46 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget module_16474205290554-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_module_16474205290554" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    
    

    
    

    
    
    




  
  
  










<div class="pwr-sec-mockup  pwr--light     lazyload" style="background-color: rgba(244, 246, 250, 1.0)">
  
  

  

    
    
    


  <div class="pwr-sec-mockup__content--pos-vert">
    <div class="page-center">
      <div class="pwr-sec-mockup__content pwr-sec-mockup__content--left" style="width: 40%;">
        
        
        <h3 class="pwr-sec__title pwr-sec__title--default pwr-sec-mockup__title" id="churn-predictor">Churn Predictor</h3>
        
        
        <span class="pwr-rich-text pwr-sec__desc pwr-sec-mockup__desc">
        <div>
<div><span data-aos="fade-in" data-aos-delay="50">Analyze your existing customer base to find who's your best customer and who is most likely to churn.</span></div>
</div></span>
        
        
        
      </div>
    </div>
  </div>
  
  <div class=" pwr--relative pwr--clearfix">
    <div class="pwr-sec-mockup__mockup pwr-sec-mockup__mockup--desktop-align-default pwr-sec-mockup__mockup--mobile-align-default pwr-sec-mockup__mockup--right  " style="width: 55vw;max-width: 950px;">
      <div class="pwr-ratio-box" style="padding-bottom: calc(0.6194347657762292 * 100%);">
      <img data-srcset="
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/mockup-2.png?width=288&amp;name=mockup-2.png 288w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/mockup-2.png?width=384&amp;name=mockup-2.png 384w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/mockup-2.png?width=496&amp;name=mockup-2.png 496w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/mockup-2.png?width=600&amp;name=mockup-2.png 600w, 
                        https://f.hubspotusercontent10.net/hub/8667013/hubfs/mockup-2.png?width=1199&amp;name=mockup-2.png 1199w" alt="mockup-2" class="pwr-sec-mockup__mockup-img lazyload" width="2583">
        </div>
    </div> 
  </div>
  
    
    
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-47 dnd_area-row-18-padding dnd-section">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-cell dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">

<div class="row-fluid-wrapper row-depth-1 row-number-48 dnd-row">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_widget_1653646544110" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    
    

    
    

    
    
    


















<div class="pwr-sec-posts pwr--light pwr-sec-posts--vertical-layout pwr--sec-padding-t-md pwr--sec-padding-b-md lazyload">
  
  

  

    
    
    


  <div class="page-center pwr--relative">
    <div class="row-fluid">
      
  
      <div class="pwr-sec-posts__intro-sec pwr-sec-posts__intro-sec--standard ">
        
        
        <h2 class="pwr-sec__title pwr-sec__title--default pwr-sec__title--narrow pwr-sec-posts__title" id="get-the-latest-from-ocean.io">Get the latest from Ocean.io</h2>
        
          
        <div class="pwr-rich-text pwr-sec__desc pwr-sec-posts__desc ">
        Read our latest insights for sales, marketers, operations professionals and updates about Ocean.io</div>
        
        
      </div>
  
 
      <div class="pwr-sec-posts__container pwr-sec-posts__container--standard pwr--neg-margin-lr-10 pwr--clearfix">
          
        
              
            
                
                
                  
                
                
<a class="pwr-post-item" href="https://blog.ocean.io/monta-efficiently-scales-into-new-markets-using-oceanio?hsLang=en" style="height: 514.719px;">
  <div class="pwr-3D-box">
    <div class="pwr-post-item__content pwr-3D-box__sensor pwr-3D-box--shaddow-on-hover pwr--colored-box ">
      <div class="pwr-post-item__img lazyload" style="background-image: url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Monta%20Case%20Study%20Cover-1.png?width=600&amp;name=Monta%20Case%20Study%20Cover-1.png);background-image: -webkit-image-set(url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Monta%20Case%20Study%20Cover-1.png?width=600&amp;name=Monta%20Case%20Study%20Cover-1.png) 1x, url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Monta%20Case%20Study%20Cover-1.png?width=1200&amp;name=Monta%20Case%20Study%20Cover-1.png) 2x);"></div>
      <div class="pwr-post-item__overlay"></div>
      <div class="pwr-post-item__info-box pwr-3D-box__info-box">
        <div class="pwr-post-item__author" id="hubspot-author_data" data-hubspot-form-id="author_data" data-hubspot-name="Blog Author">
          
          <span class="pwr-post-item__date">Jan 12, 2023 10:19:09 AM</span>
          
        </div>
        <h3 class="pwr-post-item__title pwr--toc-ignore" id="monta-efficiently-enters-new-french-market-with-ocean.io">Monta efficiently enters new French Market with Ocean.io</h3>
        <div class="pwr-post-item__desc">
          
          
            
          
          Monta uses Ocean.io to efficiently prepare pipeline and enter new French market.
          
        </div>
        <span class="pwr-post-item__more-link">Start Reading<span class="pwr-link-icon pwr--padding-l-sm"><span id="hs_cos_wrapper_widget_1653646544110_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><g id="arrow-right1_layer"><path d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"></path></g></svg></span></span></span>
      </div>
    </div>
  </div>
</a>

            
                
                
                  
                
                
<a class="pwr-post-item" href="https://blog.ocean.io/product-update-cool-features-you-will-love-jan-2023?hsLang=en" style="height: 514.719px;">
  <div class="pwr-3D-box">
    <div class="pwr-post-item__content pwr-3D-box__sensor pwr-3D-box--shaddow-on-hover pwr--colored-box ">
      <div class="pwr-post-item__img lazyload" style="background-image: url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Product%20Update%20-%20Janaury%202023.png?width=600&amp;name=Product%20Update%20-%20Janaury%202023.png);background-image: -webkit-image-set(url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Product%20Update%20-%20Janaury%202023.png?width=600&amp;name=Product%20Update%20-%20Janaury%202023.png) 1x, url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Product%20Update%20-%20Janaury%202023.png?width=1200&amp;name=Product%20Update%20-%20Janaury%202023.png) 2x);"></div>
      <div class="pwr-post-item__overlay"></div>
      <div class="pwr-post-item__info-box pwr-3D-box__info-box">
        <div class="pwr-post-item__author" id="hubspot-author_data" data-hubspot-form-id="author_data" data-hubspot-name="Blog Author">
          
          <span class="pwr-post-item__date">Jan 10, 2023 10:30:00 AM</span>
          
        </div>
        <h3 class="pwr-post-item__title pwr--toc-ignore" id="product-update-new-features-to-help-discover-your-unique-niches">Product Update: New Features to help discover YOUR unique niches</h3>
        <div class="pwr-post-item__desc">
          
          
            
          
          Many use the New Year as a time for a re-start, but we wanted to shine some light on some cool filters that you might have ...
          
        </div>
        <span class="pwr-post-item__more-link">Start Reading<span class="pwr-link-icon pwr--padding-l-sm"><span id="hs_cos_wrapper_widget_1653646544110_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><g id="arrow-right1_layer"><path d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"></path></g></svg></span></span></span>
      </div>
    </div>
  </div>
</a>

            
                
                
                  
                
                
<a class="pwr-post-item" href="https://blog.ocean.io/digiply-media-are-building-stronger-lead-lists-with-ocean.io?hsLang=en" style="height: 514.719px;">
  <div class="pwr-3D-box">
    <div class="pwr-post-item__content pwr-3D-box__sensor pwr-3D-box--shaddow-on-hover pwr--colored-box ">
      <div class="pwr-post-item__img lazyload" style="background-image: url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20152899%20%281%29.png?width=600&amp;name=Frame%20152899%20%281%29.png);background-image: -webkit-image-set(url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20152899%20%281%29.png?width=600&amp;name=Frame%20152899%20%281%29.png) 1x, url(https://8667013.fs1.hubspotusercontent-na1.net/hub/8667013/hubfs/Frame%20152899%20%281%29.png?width=1200&amp;name=Frame%20152899%20%281%29.png) 2x);"></div>
      <div class="pwr-post-item__overlay"></div>
      <div class="pwr-post-item__info-box pwr-3D-box__info-box">
        <div class="pwr-post-item__author" id="hubspot-author_data" data-hubspot-form-id="author_data" data-hubspot-name="Blog Author">
          
          <span class="pwr-post-item__date">Jan 9, 2023 9:45:13 AM</span>
          
        </div>
        <h3 class="pwr-post-item__title pwr--toc-ignore" id="digiplymedia-are-building-stronger-lead-lists-with-ocean.io">DigiPlyMedia Are Building Stronger Lead Lists with Ocean.io</h3>
        <div class="pwr-post-item__desc">
          
          
            
          
          Ocean.io provides higher quality reliable leads for Digiply Media in an industry shadowed by giants.
          
        </div>
        <span class="pwr-post-item__more-link">Start Reading<span class="pwr-link-icon pwr--padding-l-sm"><span id="hs_cos_wrapper_widget_1653646544110_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><g id="arrow-right1_layer"><path d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"></path></g></svg></span></span></span>
      </div>
    </div>
  </div>
</a>

            </div>
    </div>
  </div> 
    
    
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

<div class="row-fluid-wrapper row-depth-1 row-number-49 dnd-section dnd_area-row-19-force-full-width-section dnd_area-row-19-padding">
<div class="row-fluid ">
<div class="span12 widget-span widget-type-custom_widget dnd_area-module-8-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
<div id="hs_cos_wrapper_dnd_area-module-8" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    







    







<div class="pwr-sec-cta  pwr-sec-cta--primary pwr--sec-padding-t-md pwr--sec-padding-b-md lazyload ">
  
  

  

    
    
    
        

            
            

                
                

                <div id="shape-divider_dnd_area-module-8-1" class="pwr-shape-divider__shape pwr-shape-divider__shape--bottom ">
                    

    
    

    
    
        
        
            
        

    
    
    

    
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1360 120" preserveAspectRatio="none" class="pwr-shape-divider__svg">
        
        <path fill="#141414" opacity="1.0" d="M680 120c226.667 0 453.333-40 680-120H0c226.667 80 453.333 120 680 120z" fill-rule="evenodd"></path>
        
    </svg>



                </div>
            

            
            
            <div class="pwr-shape-divider__offset-wrapper"> 
        
        
    


  <div class="page-center pwr--align-c pwr--relative">
    
      <div class="pwr-sec-cta__hor-text-wrapper">
        
          <h2 class="pwr-sec-cta__title pwr-sec-cta__title--default pwr--toc-ignore" id="see-what-we-can-do-for-you-1">See what we can do for you</h2>
        
        
        <span class="pwr-rich-text pwr-sec-cta__desc">
        <span>Get a demo to see how much better your leads could be.</span></span>
        
      </div>
      
        <div class="pwr-sec-cta__cta--right pwr-cta pwr-cta--regular-solid-primary-background pwr-cta--long">
          <a class="cta_button" href="https://get.ocean.io/get-a-demo?hsLang=en&amp;__hstc=260949202.ebc3794741760a85fbef4b715729a749.1668437339856.1677008106364.1677144740057.45&amp;__hssc=260949202.1.1677144740057&amp;__hsfp=1432596156&amp;hsutk=ebc3794741760a85fbef4b715729a749&amp;contentType=standard-page" target="_blank" rel="noopener" title="Button Dive in">Dive in</a>                    
        </div>
      
    
  </div>
    
    
    
        
         
            </div> 
        
    

</div></div>

</div><!--end widget-span -->
</div><!--end row-->
</div><!--end row-wrapper -->

</div><!--end widget-span -->
</div>
</div>
</div>
    </div>
</main>


      
        <div data-global-resource-path="POWER x OCEANIO/templates/partials/footer.html"><footer class="footer">
	<div class="footer__container">
			<div id="hs_cos_wrapper_footer_page" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">



    
    





  




<div class="pwr-footer pwr-footer-full  pwr--dark lazyload">
  
   

  

  
  
    

    
  <div class="page-center">
    <div class="pwr-footer__content pwr-footer-full__content">
      <div class="row-fluid">
        
        <div class="pwr-footer-company-info">
          <div class="pwr-footer__logo pwr-footer__logo--large">
            
            
              
            
            
            <a href="//ocean.io?hsLang=en"><img src="https://www.ocean.io/hubfs/Logo%20light.svg" alt="Logo light" width="190" height="34"></a>
            
          </div>
          <div class="pwr-rich-text pwr-footer-company-info__desc"><p>Growth happens when you prioritize the accounts that matter most.</p>
<p><img src="https://www.ocean.io/hs-fs/hubfs/gdpr%20(1).png?width=111&amp;height=41&amp;name=gdpr%20(1).png" alt="gdpr (1)" width="111" height="41" loading="lazy" style="height: auto; max-width: 100%; width: 111px;" srcset="https://www.ocean.io/hs-fs/hubfs/gdpr%20(1).png?width=56&amp;height=21&amp;name=gdpr%20(1).png 56w, https://www.ocean.io/hs-fs/hubfs/gdpr%20(1).png?width=111&amp;height=41&amp;name=gdpr%20(1).png 111w, https://www.ocean.io/hs-fs/hubfs/gdpr%20(1).png?width=167&amp;height=62&amp;name=gdpr%20(1).png 167w, https://www.ocean.io/hs-fs/hubfs/gdpr%20(1).png?width=222&amp;height=82&amp;name=gdpr%20(1).png 222w, https://www.ocean.io/hs-fs/hubfs/gdpr%20(1).png?width=278&amp;height=103&amp;name=gdpr%20(1).png 278w, https://www.ocean.io/hs-fs/hubfs/gdpr%20(1).png?width=333&amp;height=123&amp;name=gdpr%20(1).png 333w" sizes="(max-width: 111px) 100vw, 111px"> <img src="https://www.ocean.io/hubfs/capterra.svg" alt="capterra" width="126" height="41" loading="lazy" style="height: auto; max-width: 100%; width: 126px;"></p></div>
          
          <div class="pwr-footer-company-info__icons">
            
              
                
                
                  
              
              <a href="https://twitter.com/Oceandotio" target="_blank" rel="nofollow" class="pwr-social-icon" aria-label="Social Icon">
                
                <span id="hs_cos_wrapper_footer_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" aria-hidden="true"><g id="twitter1_layer"><path d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"></path></g></svg></span>
                
              </a>
            
              
                
                
                  
              
              <a href="https://www.linkedin.com/company/ocean.io/" target="_blank" rel="nofollow" class="pwr-social-icon" aria-label="Social Icon">
                
                <span id="hs_cos_wrapper_footer_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><g id="linkedin2_layer"><path d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"></path></g></svg></span>
                
              </a>
            
              
                
                
                  
              
              <a href="https://www.facebook.com/OceanHQ" target="_blank" rel="nofollow" class="pwr-social-icon" aria-label="Social Icon">
                
                <span id="hs_cos_wrapper_footer_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><g id="facebook-square3_layer"><path d="M448 80v352c0 26.5-21.5 48-48 48h-85.3V302.8h60.6l8.7-67.6h-69.3V192c0-19.6 5.4-32.9 33.5-32.9H384V98.7c-6.2-.8-27.4-2.7-52.2-2.7-51.6 0-87 31.5-87 89.4v49.9H184v67.6h60.9V480H48c-26.5 0-48-21.5-48-48V80c0-26.5 21.5-48 48-48h352c26.5 0 48 21.5 48 48z"></path></g></svg></span>
                
              </a>
            
          </div>
          
        </div>
        
        
        
        
        <div class="pwr-footer-full__menu pwr-footer-full__menu--medium-width pwr-footer-full__menu--4col pwr-js-menu">
          <span id="hs_cos_wrapper_footer_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="menu"><div id="hs_menu_wrapper_footer_page_" class="hs-menu-wrapper active-branch no-flyouts hs-menu-flow-vertical" role="navigation" data-sitemap-name="default" data-menu-id="69270765828" aria-label="Navigation Menu">
 <ul role="menu">
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none" style="height: 316px;"><a href="javascript:;" aria-haspopup="true" aria-expanded="false" role="menuitem">Useful Links</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions" role="menuitem">Features</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions-for-marketing" role="menuitem">Solution for Marketing Teams </a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/solutions-for-sales" role="menuitem">Solution for Sales Teams</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/case-studies" role="menuitem">Case studies &amp; Testimonials</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://blog.ocean.io" role="menuitem">Blog</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/contact-us" role="menuitem">Contact </a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/about-us" role="menuitem">About Us</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/career" role="menuitem">Career</a></li>
   </ul></li>
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none" style="height: 316px;"><a href="javascript:;" aria-haspopup="true" aria-expanded="false" role="menuitem">You may also like</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/abm-strategy" role="menuitem">Account-Based Strategy</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/market-segmentation" role="menuitem">Market Segmentation</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/account-based-marketing" role="menuitem">Account-Based Marketing</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/account-based-sales" role="menuitem">Account-Based Sales</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/abm-software" role="menuitem">ABM Software</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/b2b-data" role="menuitem">B2B Data</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.ocean.io/tam" role="menuitem">Total Addressable Market (TAM)</a></li>
   </ul></li>
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none" style="height: 232px;"><a href="javascript:;" aria-haspopup="true" aria-expanded="false" role="menuitem">FREE Download</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/download-cold-email-mastery-ebook" role="menuitem">Cold Email Mastery eBook</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/download-the-agile-abm-guide" role="menuitem">Agile Account-Based Marketing</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/download-the-segmentation-checklist" role="menuitem">B2B Market Segmentation Checklist</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/download-the-abm-channels-guide" role="menuitem">8 Essential Account-Based Marketing Channels</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/download-vertical-sales-blueprint" role="menuitem">Vertical Sales Blueprint</a></li>
   </ul></li>
  <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none" style="height: 232px;"><a href="javascript:;" aria-haspopup="true" aria-expanded="false" role="menuitem">Test Our B2B Database</a>
   <ul role="menu" class="hs-menu-children-wrapper">
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/total-addressable-market-calculator" role="menuitem">Calculate Your TAM</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/request-data-sample" role="menuitem">Request Data Sample</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/request-free-trial" role="menuitem">Get Free trial</a></li>
    <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://get.ocean.io/get-a-demo" role="menuitem">Demo booking</a></li>
   </ul></li>
 </ul>
</div></span>
        </div>
        

        
      </div>
    </div>

  <div class="pwr-footer-legal">
    <div class="pwr-footer-legal__content">
      <span class="pwr-footer__item pwr-footer-legal__notice">All rights reserved</span>
      
      <span class="pwr-footer__item pwr-footer-legal__menu pwr-js-menu">
        <span id="hs_cos_wrapper_footer_page_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="menu"><div id="hs_menu_wrapper_footer_page_" class="hs-menu-wrapper active-branch no-flyouts hs-menu-flow-horizontal" role="navigation" data-sitemap-name="default" data-menu-id="69271196563" aria-label="Navigation Menu">
 <ul role="menu">
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/privacy" role="menuitem">Legal and Privacy Policy</a></li>
  <li class="hs-menu-item hs-menu-depth-1" role="none"><a href="https://www.ocean.io/gdpr" role="menuitem">GDPR</a></li>
 </ul>
</div></span>
      </span>
      </div>
    
    <div class="pwr-footer-legal__back-to-top">
      <a href="#" id="pwr-js-back-to-top" class="pwr-back-to-top" aria-label="Back to top">
        <span class="pwr-back-to-top__icon pwr-icon">
          <svg version="1.1" id="arrow_backtotop" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 18.2 11.7" xml:space="preserve">
            <polygon points="2.2,11.7 0,9.6 9.1,0 18.2,9.6 16,11.7 9.1,4.4 "></polygon>
          </svg>
        </span>
      </a>
    </div>
    
  </div>

  
    


</div></div> 
		</div>
</div></footer></div>
      
    </div>
    
<script>
(function () {
    window.addEventListener('load', function () {
        setTimeout(function () {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/_hcms/perf', true /*async*/);
            xhr.setRequestHeader("Content-type", "application/json");
            xhr.onreadystatechange = function () {
                // do nothing.
            };
            var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
            function populateNetworkInfo(name, connection, info) {
                if (name in connection) {
                    info[name] = connection[name];
                }
            }
            var networkInfo = {};
            if (connection) {
                ['type', 'effectiveType', 'downlink', 'rtt'].forEach(function(name) {
                    populateNetworkInfo(name, connection, networkInfo);
                });
            }
            var perfData = {
                url: location.href,
                portal: 8667013,
                content: 103353042004,
                group: -1,
                connection: networkInfo,
                timing: performance.timing
            };
            xhr.send(JSON.stringify(perfData));
        }, 3000);  // Execute this 3 seconds after onload.
    });
})();
</script>

<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/67734165595/1667915049950/POWER_x_OCEANIO/oceanio.min.js"></script>
<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66457994058/1673904902723/POWER_x_OCEANIO/js/third_party/JQuery-3.5.1.min.js"></script>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","308366789646459");fbq("set","agent","tmgoogletagmanager","308366789646459");fbq("track","PageView");</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=308366789646459&amp;ev=PageView&amp;noscript=1"></noscript>

<script type="text/javascript" id="hs-script-loader" src="//js.hs-scripts.com/8667013.js"></script><script type="text/javascript" id="">window.addEventListener("message",function(a){"hsFormCallback"===a.data.type&&"onFormSubmitted"===a.data.eventName&&window.dataLayer.push({event:"hubspot-form-success","hs-form-guid":a.data.id})});</script>
<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66453875227/1673904915535/POWER_x_OCEANIO/js/pwr.min.js"></script>
<script>
var hsVars = hsVars || {}; hsVars['language'] = 'en';
</script>

<script src="/hs/hsstatic/cos-i18n/static-1.53/bundles/project.js"></script>
<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/69701047225/1673904895750/POWER_x_OCEANIO/js/components/shared/scroll-shadow.min.js"></script>
<script src="/hs/hsstatic/keyboard-accessible-menu-flyouts/static-1.17/bundles/project.js"></script>

    <!--[if lte IE 8]>
    <script charset="utf-8" src="https://js.hsforms.net/forms/v2-legacy.js"></script>
    <![endif]-->

<script data-hs-allowed="true" src="/_hcms/forms/v2.js"></script>

    <script data-hs-allowed="true" data-hubspot-rendered="true">
        var options = {
            portalId: '8667013',
            formId: '3d12374d-4e1f-4753-8ee5-d74cf0c717b9',
            formInstanceId: '4284',
            pageId: '103353042004',
            region: 'na1',
            
            
            
            
            pageName: "Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales",
            
            
            redirectUrl: "https:\/\/get.ocean.io\/free-trial-signup-st2",
            
            
            
            
            
            css: '',
            target: '#hs_form_target_widget_1673529900024',
            
            
            
            
            abTestId: 73193512021,
            
            
            contentType: "standard-page",
            
            
            
            formsBaseUrl: '/_hcms/forms/',
            
            
            
            formData: {
                cssClass: 'hs-form stacked hs-custom-form'
            }
        };

        options.getExtraMetaDataBeforeSubmit = function() {
            var metadata = {};
            

            if (hbspt.targetedContentMetadata) {
                var count = hbspt.targetedContentMetadata.length;
                var targetedContentData = [];
                for (var i = 0; i < count; i++) {
                    var tc = hbspt.targetedContentMetadata[i];
                     if ( tc.length !== 3) {
                        continue;
                     }
                     targetedContentData.push({
                        definitionId: tc[0],
                        criterionId: tc[1],
                        smartTypeId: tc[2]
                     });
                }
                metadata["targetedContentMetadata"] = JSON.stringify(targetedContentData);
            }

            return metadata;
        };

        hbspt.forms.create(options);
    </script>

<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66455117867/1673904896418/POWER_x_OCEANIO/js/third_party/Waypoints.min.js"></script>
<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66454203682/1673904921177/POWER_x_OCEANIO/js/third_party/CounterUp2.min.js"></script>
<script src="https://cdn2.hubspot.net/hub/-1/hub_generated/module_assets/-35056501883/1677097378425/module_-35056501883_Video.min.js"></script>
<!-- HubSpot Video embed loader -->
<script async="" data-hs-portal-id="8667013" data-hs-ignore="true" data-cookieconsent="ignore" data-hs-page-id="103353042004" src="https://static.hsappstatic.net/video-embed/ex/loader.js"></script>
<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66458008068/1673904904914/POWER_x_OCEANIO/js/third_party/Isotope.min.js"></script>
<script src="https://www.ocean.io/hs-fs/hub/8667013/hub_generated/template_assets/66453683071/1673904910703/POWER_x_OCEANIO/js/third_party/Packery.min.js"></script>

    <script data-hs-allowed="true" data-hubspot-rendered="true">
        var options = {
            portalId: '8667013',
            formId: '4d0c3ccb-f001-471d-824b-0ba9c0f9b704',
            formInstanceId: '9300',
            pageId: '103353042004',
            region: 'na1',
            
            
            
            
            pageName: "Ocean.io | B2B Prospecting Data | ABM Targeting | Vertical Sales",
            
            
            redirectUrl: "https:\/\/www.ocean.io\/thank-you",
            
            
            
            
            
            css: '',
            target: '#hs_form_target_form_module_vert_4d0c3ccb-f001-471d-824b-0ba9c0f9b704',
            
            
            
            
            abTestId: 73193512021,
            
            
            contentType: "standard-page",
            
            
            
            formsBaseUrl: '/_hcms/forms/',
            
            
            
            formData: {
                cssClass: 'hs-form stacked hs-custom-form'
            }
        };

        options.getExtraMetaDataBeforeSubmit = function() {
            var metadata = {};
            

            if (hbspt.targetedContentMetadata) {
                var count = hbspt.targetedContentMetadata.length;
                var targetedContentData = [];
                for (var i = 0; i < count; i++) {
                    var tc = hbspt.targetedContentMetadata[i];
                     if ( tc.length !== 3) {
                        continue;
                     }
                     targetedContentData.push({
                        definitionId: tc[0],
                        criterionId: tc[1],
                        smartTypeId: tc[2]
                     });
                }
                metadata["targetedContentMetadata"] = JSON.stringify(targetedContentData);
            }

            return metadata;
        };

        hbspt.forms.create(options);
    </script>



<!-- Start of HubSpot Analytics Code -->
<script type="text/javascript">
var _hsq = _hsq || [];
_hsq.push(["setContentType", "standard-page"]);
_hsq.push(["setCanonicalUrl", "https:\/\/www.ocean.io"]);
_hsq.push(["setPageId", "103353042004"]);
_hsq.push(["setContentMetadata", {
    "contentPageId": 103353042004,
    "legacyPageId": "103353042004",
    "contentFolderId": null,
    "contentGroupId": null,
    "abTestId": 73193512021,
    "languageVariantId": 103353042004,
    "languageCode": "en",
    
}]);
</script>

<script type="text/javascript">
var _hsq = _hsq || [];
_hsq.push(["setTargetedContentMetadata", []]);

//Targeted content metadata for forms
var hbspt = hbspt || {};
hbspt.targetedContentMetadata = [];
</script>
<script type="text/javascript" id="hs-script-loader" async="" defer="" src="/hs/scriptloader/8667013.js"></script>
<!-- End of HubSpot Analytics Code -->


<script type="text/javascript">
var hsVars = {
    ticks: 1677141392478,
    page_id: 103353042004,
    
    content_group_id: 0,
    portal_id: 8667013,
    app_hs_base_url: "https://app.hubspot.com",
    cp_hs_base_url: "https://cp.hubspot.com",
    language: "en",
    analytics_page_type: "standard-page",
    analytics_page_id: "103353042004",
    category_id: 1,
    folder_id: 0,
    is_hubspot_user: false
}
</script>


<script defer="" src="/hs/hsstatic/HubspotToolsMenu/static-1.154/js/index.js"></script>

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M3TVNDT" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

 

    
    
    <script type="text/javascript">
      jQuery.event.special.touchstart = {
        setup: function( _, ns, handle ){
          this.addEventListener("touchstart", handle, { passive: true });
        }
      };
    </script>
    
    
    
    
  

<div style="width:0px; height:0px; display:none; visibility:hidden;" id="batBeacon98406462550"><img style="width:0px; height:0px; display:none; visibility:hidden;" id="batBeacon179404193199" width="0" height="0" alt="" src="https://bat.bing.com/action/0?ti=27035405&amp;tm=gtm002&amp;Ver=2&amp;mid=5a347ab4-f777-422a-a8d0-d75c14f2d51d&amp;sid=f7ad60f0b35c11edad85657ee97f8bbe&amp;vid=7d1032a0642b11eda148235b2bb707b9&amp;vids=0&amp;msclkid=N&amp;gtm_tag_source=1&amp;pi=-2084395585&amp;lg=en-GB&amp;sw=1920&amp;sh=1080&amp;sc=24&amp;tl=Ocean.io%20%7C%20B2B%20Prospecting%20Data%20%7C%20ABM%20Targeting%20%7C%20Vertical%20Sales&amp;p=https%3A%2F%2Fwww.ocean.io%2F&amp;r=&amp;lt=1171&amp;evt=pageLoad&amp;sv=1&amp;rn=102228"></div><iframe owner="archetype" title="archetype" style="display: none; visibility: hidden;"></iframe><link rel="stylesheet" href="//static.hsappstatic.net/HubspotToolsMenu/static-1.154/css/toolsmenu.css"><div role="button" class="hs-tools-menu hs-collapsed" aria-expanded="false">
        <img class="hs-sprocket" alt="HubSpot Tools Menu Toggle" src="//static.hsappstatic.net/HubspotToolsMenu/static-1.154/js/sprocket_white.svg">
        <div class="hs-dropdown">
          <div class="hs-title">HubSpot Tools</div>
          <ul>
                    <li><a target="_blank" href="https://app.hubspot.com/content/8667013/edit-beta/103353042004?utm_source=sprocket-menu">
        Edit Page
        </a></li>              <li><a target="_blank" href="https://app.hubspot.com/content-detail/8667013/site-page/103353042004/performance?utm_source=sprocket-menu">
        View Page Details
        </a></li>              <li><a target="_blank" href="https://app.hubspot.com/website/8667013/pages/site?utm_source=sprocket-menu">
        Site Pages
        </a></li>              <li><a target="_blank" href="https://app.hubspot.com/content/8667013/settings/url-mappings?utm_source=sprocket-menu">
        URL Redirects
        </a></li>              <li><a target="_blank" href="https://www.ocean.io/___context___/?portalId=8667013&amp;utm_source=sprocket-menu&amp;hs-expires=1677148339&amp;hs-version=1&amp;hs-signature=AOBq0v9cxfzGY5JBffil_GAA4Cchyg1l5A">
        Developer Info
        </a></li>              <li><a target="_blank" href="https://get.ocean.io/free-trial-signup-st2?utm_source=sprocket-menu">
        View Form Redirect Page (https://get.ocean.io/free-trial-signup-st2)
        </a></li>              <li><a target="_blank" href="https://www.ocean.io/thank-you?utm_source=sprocket-menu">
        View Form Redirect Page (Confirmation page)
        </a></li>              <li><a target="_blank" href="https://app.hubspot.com/design-manager/8667013/code/66455449622?utm_source=sprocket-menu">
        Edit Template File
        </a></li>              <li><a target="_blank" href="https://app.hubspot.com/menus/8667013/edit/83537384456">
        Edit Navigation Menu
        </a></li>      
            <li>
              <a role="button" href="#hide-menu" class="hs-menu-hider">Hide This Menu</a>
            </li>
          </ul>
        </div>
      </div><iframe id="snap8678445" src="https://tr.snapchat.com/cm/i?pid=e28560a8-8921-4c95-a806-263702bfcf60&amp;u_scsid=4ffd7b3b-0da1-4024-a7a3-9f2ba56aabcf&amp;u_sclid=38752a6a-2294-4353-bedd-76932d3da50f" style="display: none; position: absolute; overflow: hidden; width: 1px; height: 1px;"></iframe></body></html>
"""

result = html_parsing_tools.get_sentences(html, "youtube", False)
print(result["rel_alternate"])

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
