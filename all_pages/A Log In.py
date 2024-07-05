import streamlit as st
import time
import requests
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher
from ruamel.yaml import YAML
from common_config import (
    get_manager,
    set_localization,
    back_to_home,
)

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

with open("config.yaml", "r") as file:
    config = yaml.load(file)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)

_ = set_localization(st.session_state.language)

st.html(
    '<h4><i class="fa-solid fa-right-to-bracket" style="display: inline; margin: 0 10px 8px 0; width: 25px"></i>'
    + _("Log In")
    + "</h4>"
)

st.html(
    """
   <style>
   div[data-testid="stForm"] {
       border: none;
       padding: 0;
   }
   div[data-testid="stAppViewContainer"] section:nth-child(2) div[data-testid="stAppViewBlockContainer"], div[data-testid="stAppViewContainer"] section:nth-child(3) div[data-testid="stAppViewBlockContainer"] {
       position: relative !important;
       bottom: 0px !important;
   }
   </style>"""
)


def send_forgot_username_email(email, username):
    url = "https://api.brevo.com/v3/smtp/email"
    payload = {
        "sender": {"name": "WinterPixelGames", "email": "support@winterpixelgames.com"},
        "to": [{"email": email}],
        "subject": "[WinterPixelGames] " + _("Forgot Username Request"),
        "htmlContent": """
       <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
       <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
       <head>
       <!--[if gte mso 9]>
       <xml>
         <o:OfficeDocumentSettings>
           <o:AllowPNG/>
           <o:PixelsPerInch>96</o:PixelsPerInch>
         </o:OfficeDocumentSettings>
       </xml>
       <![endif]-->
         <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta name="x-apple-disable-message-reformatting">
         <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
         <title></title>
           <style type="text/css">
             @media only screen and (min-width: 620px) {
         .u-row {
           width: 600px !important;
         }
         .u-row .u-col {
           vertical-align: top;
         }
         .u-row .u-col-8p83 {
           width: 52.98px !important;
         }
         .u-row .u-col-39p99 {
           width: 239.94px !important;
         }
         .u-row .u-col-51p18 {
           width: 307.08px !important;
         }
         .u-row .u-col-100 {
           width: 600px !important;
         }
       }
       @media (max-width: 620px) {
         .u-row-container {
           max-width: 100% !important;
           padding-left: 0px !important;
           padding-right: 0px !important;
           background-color: 243c66 !important;
         }
         .u-row .u-col {
           min-width: 320px !important;
           max-width: 100% !important;
           display: block !important;
         }
         .u-row {
           width: 100% !important;
         }
         .u-col {
           width: 100% !important;
         }
         .u-col > div {
           margin: 0 auto;
         }
       }
       body {
         margin: 0;
         padding: 0;
       }
       table,
       tr,
       td {
         vertical-align: top;
         border-collapse: collapse;
       }
       p {
         margin: 0;
       }
       .ie-container table,
       .mso-container table {
         table-layout: fixed;
       }
       * {
         line-height: inherit;
       }
       a[x-apple-data-detectors='true'] {
         color: inherit !important;
         text-decoration: none !important;
       }
       table, td { color: #000000; } #u_body a { color: #161a39; text-decoration: underline; }
           </style>
       <!--[if !mso]><!--><link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->
       </head>
       <body class="clean-body u_body" style="margin: 0 ;padding: 30px 0;-webkit-text-size-adjust: 100%;background-color: #243c66;color: #000000">
         <!--[if IE]><div class="ie-container"><![endif]-->
         <!--[if mso]><div class="mso-container"><![endif]-->
         <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #243c66;width:100%" cellpadding="0" cellspacing="0">
         <tbody>
         <tr style="vertical-align: top">
           <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
           <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #243c66;"><![endif]-->
       <div class="u-row-container" style="padding: 0px;background-color: transparent">
         <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
           <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
             <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
       <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #192841;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
       <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
         <div style="background-color: #192841;height: 100%;width: 100% !important;">
         <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:25px 10px;font-family:'Baloo 2',sans-serif;" align="left">
       <table width="100%" cellpadding="0" cellspacing="0" border="0">
         <tr>
           <td style="padding-right: 0px;padding-left: 0px;" align="center">
             <a href="https://winterpixelgames.com/" target="_blank">
             <img align="center" border="0" src="https://winterpixelgames.com/static/images/email_banner.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 580px;" width="580"/>
             </a>
           </td>
         </tr>
       </table>
             </td>
           </tr>
         </tbody>
       </table>
         <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
         </div>
       </div>
       <!--[if (mso)|(IE)]></td><![endif]-->
             <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
           </div>
         </div>
         </div>
       <div class="u-row-container" style="padding: 0px;background-color: transparent">
         <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #161a39;">
           <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
             <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #161a39;"><![endif]-->
       <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #081427;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
       <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
         <div style="background-color: #081427;height: 100%;width: 100% !important;">
         <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:35px 10px 10px;font-family:'Baloo 2',sans-serif;" align="left">
       <table width="100%" cellpadding="0" cellspacing="0" border="0">
         <tr>
           <td style="padding-right: 0px;padding-left: 0px;" align="center">
             <img align="center" border="0" src="https://winterpixelgames.com/static/images/email_lock.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 10%;max-width: 58px;" width="58"/>
           </td>
         </tr>
       </table>
             </td>
           </tr>
         </tbody>
       </table>
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px 15px;font-family:'Baloo 2',sans-serif;" align="left">
         <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
           <p style="font-size: 14px; line-height: 140%; text-align: center;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><strong><span style="font-size: 28px; line-height: 39.2px; color: #ffffff;">"""
        + _("Forgot Username Request")
        + """ </span></strong></span></p>
         </div>
             </td>
           </tr>
         </tbody>
       </table>
         <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
         </div>
       </div>
       <!--[if (mso)|(IE)]></td><![endif]-->
             <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
           </div>
         </div>
         </div>
       <div class="u-row-container" style="padding: 0px;background-color: transparent">
         <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
           <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
             <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
       <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #192841;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
       <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
         <div style="background-color: #192841;height: 100%;width: 100% !important;">
         <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:20px 40px;font-family:'Baloo 2',sans-serif;" align="left">
         <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
           <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _("Hello")
        + " "
        + username
        + """,</span></p>
       <p style="font-size: 14px; line-height: 140%;"> </p>
       <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _(
            "We have sent you this email in response to your request about forgotting your username on WinterPixelGames."
        )
        + """</span></p>
       <p style="font-size: 14px; line-height: 140%;"> </p>
       <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("Your username of the associated email is ")
        + username
        + """.</span></strong></p>
       <p style="font-size: 14px; line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff;"><br /></span><span style="font-size: 18px; line-height: 25.2px; color: #ffffff;"></span></span></p>
       <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _(
            "You can now login to your account using this username and the corresponding password."
        )
        + """</span></p>
       <p style="font-size: 14px; line-height: 140%;"> </p>
       <p style="line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("Happy Gaming!")
        + """</span></p>
       <p style="line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("WinterPixelGames")
        + """</span></p>
         </div>
             </td>
           </tr>
         </tbody>
       </table>
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 40px;font-family:'Baloo 2',sans-serif;" align="left">
         <!--[if mso]><style>.v-button {background: transparent !important;}</style><![endif]-->
       <div align="center">
         <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://winterpixelgames.com/" style="height:54px; v-text-anchor:middle; width:236px;" arcsize="2%"  stroke="f" fillcolor="#081427"><w:anchorlock/><center style="color:#FFFFFF;"><![endif]-->
           <a href="https://winterpixelgames.com/" target="_blank" class="v-button" style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #081427; border-radius: 1px;-webkit-border-radius: 1px; -moz-border-radius: 1px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 14px;">
             <span style="display:block;padding:15px 40px;line-height:120%;"><span style="font-size: 18px; line-height: 21.6px;"><span style="line-height: 24px; font-family: 'Open Sans', sans-serif; font-size: 20px;"><strong><span style="line-height: 16.8px;">"""
        + _("Login")
        + """</span></strong></span><br /></span></span>
           </a>
           <!--[if mso]></center></v:roundrect><![endif]-->
       </div>
             </td>
           </tr>
         </tbody>
       </table>
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:20px 40px;font-family:'Baloo 2',sans-serif;" align="left">
         <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
           <p style="font-size: 14px; line-height: 140%;"><span style="color: #888888; font-size: 14px; line-height: 19.6px; font-family: 'Open Sans', sans-serif;"><em><span style="font-size: 16px; line-height: 22.4px;">"""
        + _(
            "Please disregard this email if you did not submit a forgot username request."
        )
        + """</span></em></span></p>
         </div>
             </td>
           </tr>
         </tbody>
       </table>
         <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
         </div>
       </div>
       <!--[if (mso)|(IE)]></td><![endif]-->
             <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
           </div>
         </div>
         </div>
       <div class="u-row-container" style="padding: 0px;background-color: transparent">
         <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #18163a;">
           <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
             <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #18163a;"><![endif]-->
       <!--[if (mso)|(IE)]><td align="center" width="307" style="background-color: #081427;width: 307px;padding: 0px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
       <div class="u-col u-col-51p18" style="max-width: 320px;min-width: 307.08px;display: table-cell;vertical-align: top;">
         <div style="background-color: #081427;height: 100%;width: 100% !important;">
         <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Baloo 2',sans-serif;" align="left">
         <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
           <p style="font-size: 14px; line-height: 140%;"><span style="font-family: 'Baloo 2', sans-serif; line-height: 19.6px;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><strong><span style="font-size: 16px; line-height: 22.4px; color: #ecf0f1;">"""
        + _("Problems or questions?")
        + """</span></strong></span><span style="font-size: 14px; line-height: 19.6px; color: #ecf0f1;"></span></span></p>
       <p style="font-size: 14px; line-height: 140%;"><a rel="noopener" href="mailto:support@winterpixelgames.com" target="_blank"><span style="color: #ffffff; line-height: 19.6px; font-family: 'Baloo 2', sans-serif;"><span style="font-size: 14px; line-height: 19.6px;">support@winterpixelgames.com</span></span></a></p>
         </div>
             </td>
           </tr>
         </tbody>
       </table>
         <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
         </div>
       </div>
       <!--[if (mso)|(IE)]></td><![endif]-->
       <!--[if (mso)|(IE)]><td align="center" width="239" style="background-color: #081427;width: 239px;padding: 10px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
       <div class="u-col u-col-39p99" style="max-width: 320px;min-width: 239.94px;display: table-cell;vertical-align: top;background: #081427">
         <div style="background-color: #081427;height: 100%;width: 100% !important;">
         <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 10px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Baloo 2',sans-serif;" align="left">
         <div style="font-size: 14px; line-height: 140%; text-align: right; word-wrap: break-word;">
           <p style="font-size: 14px; line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><span style="color: #ffffff; line-height: 19.6px;">WinterPixelGames 2024</span></span></p>
         </div>
             </td>
           </tr>
         </tbody>
       </table>
         <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
         </div>
       </div>
       <!--[if (mso)|(IE)]></td><![endif]-->
       <!--[if (mso)|(IE)]><td align="center" width="52" style="background-color: #081427;width: 52px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
       <div class="u-col u-col-8p83" style="max-width: 320px;min-width: 52.98px;display: table-cell;vertical-align: top;">
         <div style="background-color: #081427;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
         <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
       <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
         <tbody>
           <tr>
             <td style="overflow-wrap:break-word;word-break:break-word;padding:15px 10px 10px;font-family:'Baloo 2',sans-serif;" align="left">
       <div align="center">
         <div style="display: table; max-width:46px;">
         <!--[if (mso)|(IE)]><table width="46" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:46px;"><tr><![endif]-->
           <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
           <table align="center" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
             <tbody><tr style="vertical-align: top"><td align="center" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
               <a href="https://github.com/TANK8K/WinterPixelGames.com" title="GitHub" target="_blank">
                 <img src="https://winterpixelgames.com/static/images/email_github.png" alt="GitHub" title="GitHub" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
               </a>
             </td></tr>
           </tbody></table>
           <!--[if (mso)|(IE)]></td><![endif]-->
           <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
         </div>
       </div>
             </td>
           </tr>
         </tbody>
       </table>
         <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
         </div>
       </div>
       <!--[if (mso)|(IE)]></td><![endif]-->
             <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
           </div>
         </div>
         </div>
           <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
           </td>
         </tr>
         </tbody>
         </table>
         <!--[if mso]></div><![endif]-->
         <!--[if IE]></div><![endif]-->
       </body>
       </html>
   """,
    }
    headers = {
        "accept": "application/json",
        "api-key": st.secrets.brevo.api_key,
        "content-type": "application/json",
    }
    requests.post(url, json=payload, headers=headers)


def send_forgot_password_email(email, username, new_password):
    url = "https://api.brevo.com/v3/smtp/email"
    payload = {
        "sender": {"name": "WinterPixelGames", "email": "support@winterpixelgames.com"},
        "to": [{"email": email}],
        "subject": "[WinterPixelGames] " + _("Forgot Password Request"),
        "htmlContent": """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
        <head>
        <!--[if gte mso 9]>
        <xml>
          <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
          </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta name="x-apple-disable-message-reformatting">
          <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
          <title></title>
            <style type="text/css">
              @media only screen and (min-width: 620px) {
          .u-row {
            width: 600px !important;
          }
          .u-row .u-col {
            vertical-align: top;
          }
          .u-row .u-col-8p83 {
            width: 52.98px !important;
          }
          .u-row .u-col-39p99 {
            width: 239.94px !important;
          }
          .u-row .u-col-51p18 {
            width: 307.08px !important;
          }
          .u-row .u-col-100 {
            width: 600px !important;
          }
        }
        @media (max-width: 620px) {
          .u-row-container {
            max-width: 100% !important;
            padding-left: 0px !important;
            padding-right: 0px !important;
            background-color: 243c66 !important;
          }
          .u-row .u-col {
            min-width: 320px !important;
            max-width: 100% !important;
            display: block !important;
          }
          .u-row {
            width: 100% !important;
          }
          .u-col {
            width: 100% !important;
          }
          .u-col > div {
            margin: 0 auto;
          }
        }
        body {
          margin: 0;
          padding: 0;
        }
        table,
        tr,
        td {
          vertical-align: top;
          border-collapse: collapse;
        }
        p {
          margin: 0;
        }
        .ie-container table,
        .mso-container table {
          table-layout: fixed;
        }
        * {
          line-height: inherit;
        }
        a[x-apple-data-detectors='true'] {
          color: inherit !important;
          text-decoration: none !important;
        }
        table, td { color: #000000; } #u_body a { color: #161a39; text-decoration: underline; }
            </style>
        <!--[if !mso]><!--><link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->
        </head>
        <body class="clean-body u_body" style="margin: 0 ;padding: 30px 0;-webkit-text-size-adjust: 100%;background-color: #243c66;color: #000000">
          <!--[if IE]><div class="ie-container"><![endif]-->
          <!--[if mso]><div class="mso-container"><![endif]-->
          <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #243c66;width:100%" cellpadding="0" cellspacing="0">
          <tbody>
          <tr style="vertical-align: top">
            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #243c66;"><![endif]-->
        <div class="u-row-container" style="padding: 0px;background-color: transparent">
          <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
            <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
              <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #192841;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
        <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
          <div style="background-color: #192841;height: 100%;width: 100% !important;">
          <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:25px 10px;font-family:'Baloo 2',sans-serif;" align="left">
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td style="padding-right: 0px;padding-left: 0px;" align="center">
              <a href="https://winterpixelgames.com/" target="_blank">
              <img align="center" border="0" src="https://winterpixelgames.com/static/images/email_banner.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 580px;" width="580"/>
              </a>
            </td>
          </tr>
        </table>
              </td>
            </tr>
          </tbody>
        </table>
          <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
          </div>
        </div>
        <!--[if (mso)|(IE)]></td><![endif]-->
              <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
            </div>
          </div>
          </div>
        <div class="u-row-container" style="padding: 0px;background-color: transparent">
          <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #161a39;">
            <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
              <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #161a39;"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #081427;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
        <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
          <div style="background-color: #081427;height: 100%;width: 100% !important;">
          <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:35px 10px 10px;font-family:'Baloo 2',sans-serif;" align="left">
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td style="padding-right: 0px;padding-left: 0px;" align="center">
              <img align="center" border="0" src="https://winterpixelgames.com/static/images/email_lock.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 10%;max-width: 58px;" width="58"/>
            </td>
          </tr>
        </table>
              </td>
            </tr>
          </tbody>
        </table>
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px 15px;font-family:'Baloo 2',sans-serif;" align="left">
          <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
            <p style="font-size: 14px; line-height: 140%; text-align: center;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><strong><span style="font-size: 28px; line-height: 39.2px; color: #ffffff;">"""
        + _("Forgot Password Request")
        + """ </span></strong></span></p>
          </div>
              </td>
            </tr>
          </tbody>
        </table>
          <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
          </div>
        </div>
        <!--[if (mso)|(IE)]></td><![endif]-->
              <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
            </div>
          </div>
          </div>
        <div class="u-row-container" style="padding: 0px;background-color: transparent">
          <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
            <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
              <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #ffffff;"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #192841;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
        <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
          <div style="background-color: #192841;height: 100%;width: 100% !important;">
          <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:20px 40px;font-family:'Baloo 2',sans-serif;" align="left">
                
          <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
            <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _("Hello")
        + " "
        + username
        + """,</span></p>
        <p style="font-size: 14px; line-height: 140%;"> </p>
        <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _(
            "We have sent you this email in response to your request about forgotting your password on WinterPixelGames."
        )
        + """</span></p>
        <p style="font-size: 14px; line-height: 140%;"> </p>
        <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("Your new auto-generated password is ")
        + new_password
        + """.</span></strong></p>
        <p style="font-size: 14px; line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff;"><br /></span><span style="font-size: 18px; line-height: 25.2px; color: #ffffff;"></span></span></p>
        <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _(
            "You can now login to your account using this password and change it to a custom password if necessary."
        )
        + """</span></p>
        <p style="font-size: 14px; line-height: 140%;"> </p>
        <p style="line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("Happy Gaming!")
        + """</span></p>
        <p style="line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("WinterPixelGames")
        + """</span></p>
          </div>
              </td>
            </tr>
          </tbody>
        </table>
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 40px;font-family:'Baloo 2',sans-serif;" align="left">
          <!--[if mso]><style>.v-button {background: transparent !important;}</style><![endif]-->
        <div align="center">
          <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://winterpixelgames.com/" style="height:54px; v-text-anchor:middle; width:236px;" arcsize="2%"  stroke="f" fillcolor="#081427"><w:anchorlock/><center style="color:#FFFFFF;"><![endif]-->
            <a href="https://winterpixelgames.com/" target="_blank" class="v-button" style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #081427; border-radius: 1px;-webkit-border-radius: 1px; -moz-border-radius: 1px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 14px;">
              <span style="display:block;padding:15px 40px;line-height:120%;"><span style="font-size: 18px; line-height: 21.6px;"><span style="line-height: 24px; font-family: 'Open Sans', sans-serif; font-size: 20px;"><strong><span style="line-height: 16.8px;">"""
        + _("Reset Password")
        + """</span></strong></span><br /></span></span>
            </a>
            <!--[if mso]></center></v:roundrect><![endif]-->
        </div>
              </td>
            </tr>
          </tbody>
        </table>
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:20px 40px;font-family:'Baloo 2',sans-serif;" align="left">
          <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
            <p style="font-size: 14px; line-height: 140%;"><span style="color: #888888; font-size: 14px; line-height: 19.6px; font-family: 'Open Sans', sans-serif;"><em><span style="font-size: 16px; line-height: 22.4px;">"""
        + _(
            "Please disregard this email if you did not submit a forgot password request."
        )
        + """</span></em></span></p>
          </div>
              </td>
            </tr>
          </tbody>
        </table>
          <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
          </div>
        </div>
        <!--[if (mso)|(IE)]></td><![endif]-->
              <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
            </div>
          </div>
          </div>
        <div class="u-row-container" style="padding: 0px;background-color: transparent">
          <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #18163a;">
            <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
              <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #18163a;"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="307" style="background-color: #081427;width: 307px;padding: 0px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
        <div class="u-col u-col-51p18" style="max-width: 320px;min-width: 307.08px;display: table-cell;vertical-align: top;">
          <div style="background-color: #081427;height: 100%;width: 100% !important;">
          <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Baloo 2',sans-serif;" align="left">
          <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
            <p style="font-size: 14px; line-height: 140%;"><span style="font-family: 'Baloo 2', sans-serif; line-height: 19.6px;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><strong><span style="font-size: 16px; line-height: 22.4px; color: #ecf0f1;">"""
        + _("Problems or questions?")
        + """</span></strong></span><span style="font-size: 14px; line-height: 19.6px; color: #ecf0f1;"></span></span></p>
        <p style="font-size: 14px; line-height: 140%;"><a rel="noopener" href="mailto:support@winterpixelgames.com" target="_blank"><span style="color: #ffffff; line-height: 19.6px; font-family: 'Baloo 2', sans-serif;"><span style="font-size: 14px; line-height: 19.6px;">support@winterpixelgames.com</span></span></a></p>
          </div>
              </td>
            </tr>
          </tbody>
        </table>
          <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
          </div>
        </div>
        <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="239" style="background-color: #081427;width: 239px;padding: 10px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
        <div class="u-col u-col-39p99" style="max-width: 320px;min-width: 239.94px;display: table-cell;vertical-align: top;background: #081427">
          <div style="background-color: #081427;height: 100%;width: 100% !important;">
          <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 10px 0px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Baloo 2',sans-serif;" align="left">
          <div style="font-size: 14px; line-height: 140%; text-align: right; word-wrap: break-word;">
            <p style="font-size: 14px; line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><span style="color: #ffffff; line-height: 19.6px;">WinterPixelGames 2024</span></span></p>
          </div>
              </td>
            </tr>
          </tbody>
        </table>
          <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
          </div>
        </div>
        <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="52" style="background-color: #081427;width: 52px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
        <div class="u-col u-col-8p83" style="max-width: 320px;min-width: 52.98px;display: table-cell;vertical-align: top;">
          <div style="background-color: #081427;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
          <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
        <table style="font-family:'Baloo 2',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
          <tbody>
            <tr>
              <td style="overflow-wrap:break-word;word-break:break-word;padding:15px 10px 10px;font-family:'Baloo 2',sans-serif;" align="left">
        <div align="center">
          <div style="display: table; max-width:46px;">
          <!--[if (mso)|(IE)]><table width="46" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:46px;"><tr><![endif]-->
            <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
            <table align="center" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
              <tbody><tr style="vertical-align: top"><td align="center" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                <a href="https://github.com/TANK8K/WinterPixelGames.com" title="GitHub" target="_blank">
                  <img src="https://winterpixelgames.com/static/images/email_github.png" alt="GitHub" title="GitHub" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                </a>
              </td></tr>
            </tbody></table>
            <!--[if (mso)|(IE)]></td><![endif]-->
            <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
          </div>
        </div>
              </td>
            </tr>
          </tbody>
        </table>
          <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
          </div>
        </div>
        <!--[if (mso)|(IE)]></td><![endif]-->
              <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
            </div>
          </div>
          </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            </td>
          </tr>
          </tbody>
          </table>
          <!--[if mso]></div><![endif]-->
          <!--[if IE]></div><![endif]-->
        </body>
        </html>
    """,
    }
    headers = {
        "accept": "application/json",
        "api-key": st.secrets.brevo.api_key,
        "content-type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code


tab1, tab2, tab3 = st.tabs(
    [
        "**" + _("Login") + "**",
        "**" + _("Forgot Username") + "**",
        "**" + _("Forgot Password") + "**",
    ]
)
with tab1:
    authenticator.login(
        fields={
            "Form name": _("Login"),
            "Username": _("Username"),
            "Password": _("Password"),
            "Login": _("Login"),
        },
    )
    if st.session_state["authentication_status"] == False:
        st.error(_("Username or Password is incorrect"))

    elif st.session_state["authentication_status"] == True:
        try:
            cookie_manager = get_manager("store_username")
            cookie_manager.set(
                "username", st.session_state.username, key="cookie_username"
            )
        except Exception:
            pass
        try:
            cookie_manager_2 = get_manager("store_name")
            cookie_manager_2.set("name", st.session_state.name, key="cookie_name")
        except Exception:
            pass
        time.sleep(1)
        with open("config.yaml", "w") as file:
            yaml.dump(config, file)
        time.sleep(1)
        st.switch_page("all_pages/0 Home.py")


with tab2:
    try:
        username_of_forgotten_username, email_of_forgotten_username = (
            authenticator.forgot_username(
                fields={
                    "Form name": _("Forgot Username"),
                    "Email": _("Email"),
                    "Submit": _("Send Userename"),
                }
            )
        )
        if username_of_forgotten_username:
            send_forgot_username_email(
                email_of_forgotten_username,
                username_of_forgotten_username,
            )
            st.success(_("Username is sent to the associated email successfully"))
        elif username_of_forgotten_username == False:
            st.error(_("Email not found"))
    except Exception as e:
        st.error(e)

with tab3:
    try:
        (
            username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password,
        ) = authenticator.forgot_password(
            fields={
                "Form name": _("Forgot Password"),
                "Username": _("Username"),
                "Submit": _("Reset Password"),
            }
        )
        if username_of_forgotten_password:
            send_forgot_password_email(
                email_of_forgotten_password,
                username_of_forgotten_password,
                new_random_password,
            )
            config["credentials"]["usernames"][username_of_forgotten_password][
                "password"
            ] = Hasher._hash(new_random_password)
            with open("config.yaml", "w") as file:
                yaml.dump(config, file)
            st.success(_("New password is sent to the associated email successfully"))
        elif username_of_forgotten_password == False:
            st.error(_("Username not found"))
    except Exception as e:
        st.error(e)

st.info(_("Click the button again if it doesn't work for the first time"))
back_to_home(st.session_state.language)
