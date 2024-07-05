import streamlit as st
import time
import re
import requests
import random
import string
import streamlit_authenticator as stauth
from ruamel.yaml import YAML
from streamlit_js_eval import streamlit_js_eval
from common_config import (
    set_localization,
    back_to_home,
)

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

_ = set_localization(st.session_state.language)


st.html(
    '<h4><i class="fa-solid fa-user-plus" style="display: inline; margin: 0 10px 8px 0; width: 25px"></i>'
    + _("Sign Up")
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


def generate_verification_code(length=8):
    characters = string.ascii_uppercase + string.digits
    characters = (
        characters.replace("0", "").replace("O", "").replace("I", "").replace("1", "")
    )

    verification_code = "".join(random.choice(characters) for _ in range(length))
    return verification_code


def send_verification_code_email(email, verification_code):
    url = "https://api.brevo.com/v3/smtp/email"
    payload = {
        "sender": {"name": "WinterPixelGames", "email": "support@winterpixelgames.com"},
        "to": [{"email": email}],
        "subject": "[WinterPixelGames] " + _("Verify Account"),
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
             <img align="center" border="0" src="https://winterpixelgames.com/static/images/email_verify.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 10%;max-width: 58px;" width="58"/>
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
        + _("Verify Account")
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
        + """,</span></p>
       <p style="font-size: 14px; line-height: 140%;"> </p>
       <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _(
            "Welcome to WinterPixelGames! We're excited to have you join our community. Before you creating your account, we need to verify your email address to ensure we have the correct information."
        )
        + """</span></p>
       <p style="font-size: 14px; line-height: 140%;"> </p>
       <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("Your verification code is ")
        + verification_code
        + """.</span></strong></p>
       <p style="font-size: 14px; line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 19.6px;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff;"><br /></span><span style="font-size: 18px; line-height: 25.2px; color: #ffffff;"></span></span></p>
       <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px; color: #ffffff; font-family: 'Open Sans', sans-serif;">"""
        + _(
            "You can now register your account using this verification code and the corresponding email."
        )
        + """</span></p>
       <p style="font-size: 14px; line-height: 140%;"> </p>
       <p style="line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">"""
        + _("Happy Gaming!")
        + """</span></p>
       <p style="line-height: 140%;"><span style="font-family: 'Open Sans', sans-serif; line-height: 25.2px; font-size: 18px; color: #ffffff;">WinterPixelGames</span></p>
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
        + _("Verify")
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
        + _("Please disregard this email if you did not submit a verify email request.")
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


def validate_email(email_to_check):
    if email_to_check == "":
        return "Email is required"

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    correct_email_format = re.match(pattern, email_to_check) is not None

    if not correct_email_format:
        return "Email is not valid"

    else:
        with open("config.yaml", "r") as file:
            config = yaml.load(file)

        for username, details in (
            config.get("credentials", {}).get("usernames", {}).items()
        ):
            if details.get("email") == email_to_check:
                return "Email is already in use"
        return "Email can be registered"


tab1, tab2 = st.tabs(
    [
        "**" + _("Verify Email") + "**",
        "**" + _("Register") + "**",
    ]
)

with tab1:
    try:
        st.markdown("### " + _("Verify Email"))

        email_to_be_registered = st.text_input(_("Email"), max_chars=255)
        verification_code = st.text_input(
            _("Verification Code"),
            max_chars=8,
            placeholder=_("Leave it blank to send Verification Code"),
        )
        verify_button = st.button(_("Send/Verify"))

        if verify_button:
            if verification_code != "":
                with open("config.yaml", "r") as file:
                    config = yaml.load(file)

                if email_to_be_registered not in config["verification"]:
                    st.error(_("Email not found"))
                elif (
                    config["verification"][email_to_be_registered] != verification_code
                ):
                    st.error(_("Wrong verification code"))
                elif (
                    config["verification"][email_to_be_registered] == verification_code
                ):
                    del config["verification"][email_to_be_registered]
                    config["pre-authorized"]["emails"].append(email_to_be_registered)
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)
                    st.success(_("Verify success"))
                    time.sleep(1)
            else:
                generated_verification_code = generate_verification_code()
                sign_up_check_status = validate_email(email_to_be_registered)
                if sign_up_check_status == "Email can be registered":
                    send_verification_code_email(
                        email_to_be_registered,
                        generated_verification_code,
                    )
                    with open("config.yaml", "r") as file:
                        config = yaml.load(file)

                    config["verification"][
                        email_to_be_registered
                    ] = generated_verification_code

                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)

                    st.success(_("Verification code is sent to the email successfully"))
                    # time.sleep(1)
                    # streamlit_js_eval(js_expressions="parent.window.location.reload()")
                elif sign_up_check_status == "Email is required":
                    st.error(_("Email is required"))
                elif sign_up_check_status == "Email is not valid":
                    st.error(_("Email is not valid"))
                elif sign_up_check_status == "Email is already in use":
                    st.error(_("Email is already in use"))

    except Exception as e:
        st.error(e)


with tab2:
    try:
        with open("config.yaml", "r") as file:
            config = yaml.load(file)
        authenticator = stauth.Authenticate(
            config["credentials"],
            config["cookie"]["name"],
            config["cookie"]["key"],
            config["cookie"]["expiry_days"],
            config["pre-authorized"],
        )
        (
            email_of_registered_user,
            username_of_registered_user,
            name_of_registered_user,
        ) = authenticator.register_user(
            pre_authorization=True,
            fields={
                "Form name": _("Register"),
                "Name": _("Nickname") + " (" + _("alphabets only") + ")",
                "Email": _("Verified Email"),
                "Username": _("Username") + " (" + _("for login") + ")",
                "Password": _("Password") + " (" + _("for login") + ")",
                "Repeat password": _("Repeat Password"),
                "Register": _("Register"),
            },
        )
        if name_of_registered_user:
            st.success(_("User registered successfully"))
            with open("config.yaml", "w") as file:
                yaml.dump(config, file)
                time.sleep(1)
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
    except Exception as e:
        st.error(e)

back_to_home(st.session_state.language)
