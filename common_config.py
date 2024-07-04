import streamlit as st
import extra_streamlit_components as stx
import streamlit_authenticator as stauth
import gettext
import time
import requests
from ruamel.yaml import YAML
import random
import string
import uuid
import re
from streamlit_authenticator.utilities.hasher import Hasher
from streamlit_js_eval import streamlit_js_eval

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True


def get_manager(key):
    return stx.CookieManager(key)


def validate_user_id(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False


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


def set_localization(language):
    try:
        localizator = gettext.translation(
            f"base_{language}", localedir="locales", languages=[language]
        )
        localizator.install()
        _ = localizator.gettext
    except Exception:
        _ = gettext.gettext
    return _


def available_languages():
    cookie_manager = get_manager("available_languages")
    locale = cookie_manager.get(cookie="locale")

    if locale is not None:
        st.session_state.language = locale
    else:
        st.session_state.language = "english"
    if st.sidebar.button("​", use_container_width=True):
        try:
            pop_choose_language(_)
        except Exception as e:
            print(e)


available_languages()
_ = set_localization(st.session_state.language)


@st.experimental_dialog(" ")
def pop_account(selected_language):
    cookie_manager = get_manager("pop_account")
    logged_in_user_username = cookie_manager.get(cookie="username")
    saved_account = cookie_manager.get(cookie="account")

    _ = set_localization(selected_language)

    with open("config.yaml", "r") as file:
        config = yaml.load(file)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["pre-authorized"],
    )
    tab1, tab2, tab3 = st.tabs(
        [
            "**" + _("Linked Game Accounts") + "**",
            "**" + _("Change Nickname/Email") + "**",
            "**" + _("Change Password") + "**",
        ]
    )
    with tab1:
        with st.form("Linked Game Accounts"):
            st.markdown("### " + _("Linked Game Accounts"))
            st.info(
                _(
                    "Statistics of Linked Accounts will be tracked daily and displayed in Player Info"
                )
                + " ("
                + _("WIP")
                + ")",
                icon="ℹ️",
            )
            try:
                user_id_RBR_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_RBR"]
            except KeyError:
                user_id_RBR_record = "No Records Found"
            try:
                user_id_GD_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_GD"]
            except KeyError:
                user_id_GD_record = "No Records Found"
            try:
                user_id_GR_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_GR"]
            except KeyError:
                user_id_GR_record = "No Records Found"
            try:
                user_id_GS_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_GS"]
            except KeyError:
                user_id_GS_record = "No Records Found"

            user_id_RBR = st.text_input(
                "**" + _("Rocket Bot Royale") + "**",
                placeholder=user_id_RBR_record,
                max_chars=36,
            )
            user_id_GD = st.text_input(
                "**" + _("Goober Dash") + "**",
                placeholder=user_id_GD_record,
                max_chars=36,
            )
            user_id_GR = st.text_input(
                "**" + _("Goober Royale") + "**",
                placeholder=user_id_GR_record,
                max_chars=36,
            )
            user_id_GS = st.text_input(
                "**" + _("Goober Shot") + "**",
                placeholder=user_id_GS_record,
                max_chars=36,
            )
            user_id_dict = {
                "user_id_RBR": user_id_RBR,
                "user_id_GD": user_id_GD,
                "user_id_GR": user_id_GR,
                "user_id_GS": user_id_GS,
            }
            convert_to_game_name_dict = {
                "user_id_RBR": _("Rocket Bot Royale"),
                "user_id_GD": _("Goober Dash"),
                "user_id_GR": _("Goober Royale"),
                "user_id_GS": _("Goober Shot"),
            }
            Update_button = st.form_submit_button(_("Update"))
            if Update_button:
                correct_format_all = True
                for key in user_id_dict:
                    if user_id_dict[key] != "":
                        if not validate_user_id(user_id_dict[key]):
                            st.error(
                                _("Wrong User ID format of ")
                                + convert_to_game_name_dict[key]
                            )
                            correct_format_all = False
                            break
                        else:
                            config["credentials"]["usernames"][logged_in_user_username][
                                key
                            ] = user_id_dict[key]
                if correct_format_all:
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)
                    st.success(_("User IDs are updated successfully"))
    with tab2:
        if saved_account is not None:
            try:
                if authenticator.update_user_details(
                    logged_in_user_username,
                    fields={
                        "Form name": _("Change Name/Email"),
                        "Field": _("Field"),
                        "Name": _("Nickname"),
                        "Email": _("Email"),
                        "New value": _("New value"),
                        "Update": _("Update"),
                    },
                ):
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)
                    st.success(_("Entries updated successfully"))
            except Exception as e:
                st.error(e)

    with tab3:
        if saved_account is not None:
            try:
                if authenticator.reset_password(
                    logged_in_user_username,
                    fields={
                        "Form name": _("Change Password"),
                        "Current password": _("Current Password"),
                        "New password": _("New Password"),
                        "Repeat password": _("Repeat Password"),
                        "Reset": _("Reset"),
                    },
                ):
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)
                    st.success(_("Password modified successfully"))
            except Exception as e:
                st.error(e)


@st.experimental_dialog(" ")
def pop_log_in(selected_language):
    cookie_manager = get_manager("pop_log_in")

    _ = set_localization(selected_language)

    with open("config.yaml", "r") as file:
        config = yaml.load(file)

    tab1, tab2, tab3 = st.tabs(
        [
            "**" + _("Login") + "**",
            "**" + _("Forgot Username") + "**",
            "**" + _("Forgot Password") + "**",
        ]
    )
    with tab1:
        with open("config.yaml", "r") as file:
            yaml.load(file)

        authenticator = stauth.Authenticate(
            config["credentials"],
            config["cookie"]["name"],
            config["cookie"]["key"],
            config["cookie"]["expiry_days"],
            config["pre-authorized"],
        )
        authenticator.login(
            fields={
                "Form name": _("Login"),
                "Username": _("Username"),
                "Password": _("Password"),
                "Login": _("Login"),
            }
        )

        cookie_manager.set("username", st.session_state["username"], key="15")
        cookie_manager.set("name", st.session_state["name"], key="16")

        if st.session_state["authentication_status"] == False:
            st.error(_("Username or Password is incorrect"))

        elif st.session_state["authentication_status"] == True:
            with open("config.yaml", "w") as file:
                yaml.dump(config, file)
            time.sleep(0.25)
            streamlit_js_eval(js_expressions="parent.window.location.reload()")

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
                st.success(
                    _("New password is sent to the associated email successfully")
                )
            elif username_of_forgotten_password == False:
                st.error(_("Username not found"))
        except Exception as e:
            st.error(e)


@st.experimental_dialog(" ")
def pop_sign_up(selected_language):
    _ = set_localization(selected_language)

    tab1, tab2 = st.tabs(
        [
            "**" + _("Verify Email") + "**",
            "**" + _("Register") + "**",
        ]
    )
    with tab1:
        try:
            generated_verification_code = generate_verification_code()

            with st.form("Verify Email"):
                st.markdown("### " + _("Verify Email"))
                email_to_be_registered = st.text_input(_("Email"), max_chars=255)

                if not st.session_state["verification_code_sent"]:
                    send_verification_code = st.form_submit_button(
                        _("Send Verification Code")
                    )
                else:
                    verification_code = st.text_input(
                        _("Verification Code"), max_chars=8
                    )
                    verify_email = st.form_submit_button(_("Verify Email"))

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

                if not st.session_state["verification_code_sent"]:
                    if send_verification_code:
                        sign_up_check_status = validate_email(email_to_be_registered)
                        if sign_up_check_status == "Email can be registered":
                            send_verification_code_email(
                                email_to_be_registered,
                                generated_verification_code,
                            )
                            st.session_state["verification_code_sent"] = True

                            with open("config.yaml", "r") as file:
                                config = yaml.load(file)

                            config["verification"][
                                email_to_be_registered
                            ] = generated_verification_code

                            with open("config.yaml", "w") as file:
                                yaml.dump(config, file)

                            st.success(
                                _("Verification code is sent to the email successfully")
                            )
                            time.sleep(1)
                            st.rerun()
                        elif sign_up_check_status == "Email is required":
                            st.error(_("Email is required"))
                        elif sign_up_check_status == "Email is not valid":
                            st.error(_("Email is not valid"))
                        elif sign_up_check_status == "Email is already in use":
                            st.error(_("Email is already in use"))
                else:
                    if verify_email:
                        with open("config.yaml", "r") as file:
                            config = yaml.load(file)

                        if email_to_be_registered not in config["verification"]:
                            st.error(_("Email not found"))
                        elif (
                            config["verification"][email_to_be_registered]
                            != verification_code
                        ):
                            st.error(_("Wrong verification code"))
                        elif (
                            config["verification"][email_to_be_registered]
                            == verification_code
                        ):
                            del config["verification"][email_to_be_registered]
                            config["pre-authorized"]["emails"].append(
                                email_to_be_registered
                            )
                            with open("config.yaml", "w") as file:
                                yaml.dump(config, file)
                            st.success(_("Verify success"))
                            time.sleep(1)
                            st.rerun()

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
                    "Email": _("Verified Email")
                    + " ("
                    + _("used for forgot username/password")
                    + ")",
                    "Username": _("Username") + " (" + _("used for login") + ")",
                    "Password": _("Password") + " (" + _("used for login") + ")",
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


def account_system(_):
    cookie_manager = get_manager("account_system")
    logged_in_user_username = cookie_manager.get(cookie="username")
    logged_in_user_name = cookie_manager.get(cookie="name")
    saved_account = cookie_manager.get(cookie="account")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if "welcome_sent" not in st.session_state:
        st.session_state["welcome_sent"] = False

    if st.session_state["logged_in"]:
        streamlit_js_eval(js_expressions="parent.window.location.reload()")

    if saved_account is not None and not st.session_state["welcome_sent"]:
        try:
            st.toast(
                "**" + _("Welcome back") + f", {logged_in_user_name}!**", icon="🥳"
            )
            st.session_state["welcome_sent"] = True
        except Exception:
            pass
    if saved_account is not None:
        st.sidebar.write("")
        col3, col4 = st.sidebar.columns((5, 5))
        with col3:
            if st.button("​​​​", use_container_width=True, type="primary"):
                try:
                    with open("config.yaml", "r") as file:
                        config = yaml.load(file)
                    config["credentials"]["usernames"][logged_in_user_username][
                        "logged_in"
                    ] = False
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)

                    st.session_state["logged_in"] = True
                    saved_account = cookie_manager.delete(cookie="account")

                except Exception as e:
                    print(e)
        with col4:
            if st.button("​​​​​", use_container_width=True, type="primary"):
                try:
                    pop_account(st.session_state.language)
                except Exception as e:
                    print(e)
                    pass
    if saved_account is None:
        col1, col2 = st.sidebar.columns((5, 5))
        with col1:
            if st.button("​​​", use_container_width=True, type="primary"):
                try:
                    pop_log_in(st.session_state.language)
                except Exception as e:
                    print(e)
                    pass
        with col2:
            if st.button("​​", use_container_width=True, type="primary"):
                try:
                    pop_sign_up(st.session_state.language)
                except Exception as e:
                    print(e)
                    pass


@st.experimental_dialog(" ")
def pop_choose_language(_):
    cookie_manager = get_manager("pop_choose_language")

    _ = set_localization(st.session_state.language)
    languages_dict = {
        "english": "🇺🇸 English ✅",
        "zh-TW": "🇹🇼 繁體中文 ✅",
        "zh-CN": "🇨🇳 簡体中文 ✅",
        "fr": "🇫🇷 Français 🚧",
        "es-ES": "🇪🇸 Español 🚧",
        "it": "🇮🇹 Italiano 🚧",
        "de": "🇩🇪 Deutsch 🚧",
        "nl": "🇳🇱 Nederlands 🚧",
        "pt-PT": "🇵🇹 Português 🚧",
        "pt-BR": "🇧🇷 Português brasileir 🚧",
        "da": "🇩🇰 Dansk 🚧",
        "nb": "🇳🇴 Norsk bokmål 🚧",
        "no": "🇳🇴 Norsk 🚧",
        "sv-SE": "🇸🇪 Svenska 🚧",
        "fi": "🇫🇮 Suomi 🚧",
        "pl": "🇵🇱 Polski 🚧",
        "uk": "🇺🇦 Українська 🚧",
        "ru": "🇷🇺 Русский 🚧",
        "sk": "🇸🇰 Slovenský 🚧",
        "sl": "🇸🇮 Slovenščina 🚧",
        "bg": "🇧🇬 Български 🚧",
        "cs": "🇨🇿 Čeština 🚧",
        "ro": "🇷🇴 Română 🚧",
        "et": "🇪🇪 Eesti 🚧",
        "el": "🇬🇷 Ελληνική 🚧",
        "hu": "🇭🇺 Magyar 🚧",
        "lv": "🇱🇻 Latviešu 🚧",
        "lt": "🇱🇹 Lietuvių 🚧",
        "tr": "🇹🇷 Türkçe 🚧",
        "id": "🇮🇩 Bahasa Indonesia 🚧",
        "ar": "🇸🇦 العربية 🚧",
        "ko": "🇰🇷 한국어 🚧",
        "ja": "🇯🇵 日本語 🚧",
    }

    languages = [language for language in languages_dict]
    languages.insert(0, languages.pop(languages.index(st.session_state.language)))

    st.session_state.language = st.selectbox(
        " ",
        languages,
        format_func=lambda x: languages_dict.get(x),
        label_visibility="collapsed",
    )
    cookie_manager.set("locale", st.session_state.language)

    if st.button("**" + _("Apply") + "**", use_container_width=True):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")

    with st.expander(_("Contributors") + """ (""" + _("In no particular order") + ")"):
        st.link_button(
            "Stickman A",
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
        st.link_button(
            "shimobri",
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
        st.link_button(
            "TANK8K",
            "https://github.com/TANK8K/",
        )

    st.link_button(
        _("Contribute"),
        "https://translate.winterpixelgames.com/",
        type="primary",
        use_container_width=True,
    )


try:
    _ = set_localization(st.session_state.language)
except Exception:
    _ = set_localization("english")


def back_to_home(selected_language):
    _ = set_localization(selected_language)
    st.html(
        """<style>
            div[data-testid="stPageLink"] p::before { 
                font-family: "Font Awesome 5 Free" !important;
                content: "\\f015";
                display: inline-block;
                vertical-align: middle;
                font-weight: 700;
                font-size: 18px;
                font-family: 'Baloo 2';
                color: white;
                padding-right: 8px;
            }
            div[data-testid="stPageLink"] p { 
                position: absolute;
                right: 50%;
                transform: translateX(50%);
                padding: 3px 10px;
                font-weight: 800;
                font-size: 18px !important;
                color: white;
                outline: none;
                background-color: rgb(10, 26, 51);
                border-radius: 0.5rem;
                border: 2px solid #2b3d58;
            }
            div[data-testid="stPageLink"] p:hover { 
                border: 2px solid #158fd8;
                box-shadow: 0 0 10px #158fd8;
            }
            div[data-testid="stPageLink"] p:active { 
                background-color: #192841;
            }</style>"""
    )
    st.divider()
    st.page_link("./all_pages/0 Home.py", label=_("Back to Home"))


def back_to_menu(selected_language):
    _ = set_localization(selected_language)

    def to_menu_page():
        st.session_state.page = "menu"

    st.html(
        """<style>
            div[data-testid="stAppViewBlockContainer"] div[data-testid="stVerticalBlock"]  div[data-testid="element-container"]:last-child div[data-testid="stButton"] button[data-testid="baseButton-secondary"]:nth-last-child(1) p::before { 
                font-family: "Font Awesome 5 Free" !important;
                content: "\\f0c9";
                display: inline-block;
                vertical-align: middle;
                font-weight: 900;
                font-size: 18px;
                color: white;
                padding-right: 8px;
            }
            div[data-testid="stAppViewBlockContainer"] div[data-testid="stButton"] button:nth-last-child(1) p { 
                font-weight: 900;
                font-size: 18px;
            }
            div[data-testid="stAppViewBlockContainer"] div[data-testid="stButton"] button[data-testid="baseButton-secondary"]:nth-last-child(1) { 
                position: absolute;
                right: 50%;
                transform: translateX(50%);
                padding: 5px 10px;
                border-radius: 0.5rem;
                border: 2px solid #2b3d58;
            }
            div[data-testid="stAppViewBlockContainer"] button[data-testid="baseButton-secondary"]:nth-last-child(1):hover { 
                border: 2px solid #158fd8;
                box-shadow: 0 0 10px #158fd8;
            }
            div[data-testid="stAppViewBlockContainer"] button[data-testid="baseButton-secondary"]:nth-last-child(1):active { 
                background-color: #192841;
            }</style>"""
    )
    st.divider()
    st.button(_("Back to Menu"), on_click=to_menu_page)


def main_config():
    if "verification_code_sent" not in st.session_state:
        st.session_state["verification_code_sent"] = False

    if st.session_state["verification_code_sent"]:
        pop_sign_up(_)

    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = None

    st.logo(
        "static/streamlit_banner_v4.png",
        icon_image="static/wpg_hex_logo_144.png",
    )
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"> 
        <style>
        *:hover {
            cursor: url('./app/static/cursor_v5.png'), auto !important;
        }
        *:focus {
            cursor: url('./app/static/cursor_v5.png'), auto !important;
        }
        body * {
            word-break: break-word;
        }
        a {
            text-decoration: none !important;
        }
        h1, h2, h3, h4, h5, h6, p, li, table, div[class="stHtml"] {
            font-family: 'Baloo 2' !important;
        }
        h3, h4 {
            font-weight: 800;
            font-size: 25px;
        }
        h3 {
            color: #32bafa;
        }
        h3, h4 {
            padding: 0;
        }
        section[data-testid="stSidebar"] {
            #width: 350px !important;
            padding-right: 3px !important;
            user-select: none !important;
        }
        div[data-testid="stSidebarNav"] > ul[data-testid="stSidebarNavItems"] > li > div > a > span {
            color: white !important;
            font-weight: 700;
            font-size: 25px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(1) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f015";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 20px;
            color: white;
            min-width: 35px;
            padding-left: 8px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(2) > div > a::before{
            content: "";
            background-image: url("./app/static/RocketBotRoyale/rocket_bot_royale_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(3) > div > a::before{
            content: "";
            background-image: url("./app/static/GooberDash/goober_dash_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(4) > div > a::before{
            content: "";
            background-image: url("./app/static/GooberRoyale/goober_royale_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(5) > div > a::before{
            content: "";
            background-image: url("./app/static/GooberShot/goober_shot_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(6) > div > a::before{
            content: "";
            background-image: url("./app/static/MoonrockMiners/moonrock_miners_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(7) > div > a::before{
            content: "";
            background-image: url("./app/static/Broski/broski_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(8) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f05a";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 25px;
            color: white;
            min-width: 35px;
            padding-left: 6px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(9) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f08e";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 20px;
            color: white;
            min-width: 35px;
            padding-left: 7px;
        }
        header {
            background: transparent !important;
        }
        button[data-baseweb="tab"] {
            color: #ffffff !important; 
        }
        div[data-baseweb="tab-list"] > div[data-baseweb="tab-highlight"] {
            background-color: #3097e6 !important;
        }
        div[data-testid="stSidebarHeader"] img[data-testid="stLogo"] {
            width: 100%;
            height: 100%;
            left: 12px;
            position: relative;
            transform: scale(1.2, 1.2);
            top: 15px;
        }
        div[data-testid="stDecoration"] {
            background-image: linear-gradient(90deg, rgb(0, 108, 176), rgb(0, 43, 71));
        }
        ul[data-testid="main-menu-list"] > ul:nth-child(4) {
            display: none;
        }
        ul[data-testid="main-menu-list"] > div[data-testid="main-menu-divider"] {
            display: none;
        } 
        body {
            overscroll-behavior-x: none !important;
            overscroll-behavior-y: none !important;
        }
        div[data-testid="collapsedControl"] {
            z-index: 9999999;
            left: 0.5rem;
        }
        div[data-testid="collapsedControl"] > div {
            padding-top: 8px;
            left: -3px;
            position: relative;
        }
        div[data-testid="stSidebarCollapseButton"] {
            position: relative;
            top: 25px;
            left: 25px;
        }
        div[data-testid="stSidebarCollapseButton"] > button[data-testid="baseButton-header"], button[data-testid="baseButton-headerNoPadding"] {
            border-radius: 50px;
        }
        div[data-testid="collapsedControl"] > button[data-testid="baseButton-headerNoPadding"] > svg {
            font-size: 1rem;
            position: relative;
        }
        * {
            cursor: url('./app/static/cursor_v5.png'), auto !important;
        }
        @supports not selector(::-webkit-scrollbar) {
            html {
                scrollbar-color: rgb(108, 195, 251) transparent !important;
            }
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar {
            width: 6px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-track {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3) !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 0.8), rgba(50, 144, 212, 0.8)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb:hover {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 0.9), rgba(50, 144, 212, 0.9)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb:active {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 1), rgba(50, 144, 212, 1)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 33px;
            color: white;
            text-align: center;
            background-color: #081427;
            z-index: 99999;
            border-top: 1px solid #384251;
        }
        .footer > p {
            font-size: 0.7rem !important;
            line-height: 15px;
            margin-top: 2px;
        }
        div[data-testid="collapsedControl"] > div > button {
            margin: 0;
            position: relative;
            top: -2px;
            padding-left: 50px;
            left: -50px;
            transform: translateX(50px);
        }
        div[data-testid="collapsedControl"] button:hover {
            background-color: transparent;
        }
        div[data-testid="collapsedControl"]:hover {
            border-color: #158fd8;
            box-shadow: 0 0 12px #158fd8;
            transform: translateX(-10px);
            -webkit-transform:translateX(-10px);
            transition: 0.2s ease-in-out;
            -wenkit-transition: 0.2s ease-in-out;
            opacity: 1;
        }
        div[data-testid="collapsedControl"] {
            background: #192841;
            margin-left: -50px;
            left: -10px;
            padding: 3px 0 3px 30px;
            border: 1px solid #32bafa;
            border-radius: 50px;
            top: 35px;
            transform: translateX(-50px);
            opacity: 0.5;
        }
        div[data-testid="collapsedControl"] img {
            top: 6px;
            position: relative;
            left: -1px;
            transform: translateX(50px) scale(1.5,1.5);
        }
        div[data-testid="stAppViewBlockContainer"] p {
            font-size: 1.3rem;
        }
        hr:not([size]) {
            height: 1px;
            margin: 1rem 0px;
        }
        a[data-testid="baseLinkButton-primary"]:hover, a[data-testid="baseLinkButton-secondary"]:hover, div[data-testid="stVerticalBlock"] div:not([data-baseweb]) button:hover {
            color: white;
            outline: none;
            border: 1.5px solid #158fd8;
            box-shadow: 0 0 10px #158fd8;
        }
        a[data-testid="baseLinkButton-primary"]:focus, a[data-testid="baseLinkButton-secondary"]:focus, button:focus {
            color: white !important;
        }
        div[data-baseweb="tab-list"] button:hover {
            color: #158fd8 !important;    
            border: none !important;
            box-shadow: none !important;
        }
        section[data-testid="stSidebar"] > div:nth-child(2) > div > div {
            display: none;
        }
        div[data-testid="stAppViewBlockContainer"] {
            padding: 0px 5vw 100px 5vw !important;
        }
        div[data-testid="stNotification"] {
            padding: 10px;
        }
        div[data-testid="stAppViewBlockContainer"] div[data-testid="stFullScreenFrame"]:first-child > div {
            justify-content: center;
        }
        div[data-testid="stNotification"] {
            width: fit-content;
        }
        summary:hover {
            color: rgb(48, 151, 230) !important;
        }
        ul[data-testid="stSidebarNavItems"] {
            max-height: none !important;
            list-style: none !important;
            overflow: auto !important;
            margin: 0px !important;
            padding-bottom: 0.125rem !important;
        }
        div[data-testid="stSidebarNavSeparator"] {
            display: none;
        }
        div[data-testid="stToast"] {
            background: #192841;
            box-shadow: 0 0 10px #158fd8;
            border: 1px solid #158fd8;
        }
        div[role="dialog"] div[data-testid="stForm"] {
            border: none;
            padding: 0;
        }
        div[data-testid="stAppViewContainer"] section:nth-child(2) div[data-testid="stAppViewBlockContainer"], div[data-testid="stAppViewContainer"] section:nth-child(3) div[data-testid="stAppViewBlockContainer"] {
            position: relative !important;
            bottom: 50px !important;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


def footer_account_language(selected_language):
    _ = set_localization(selected_language)
    st.markdown(
        (
            """
            <div class="footer">
            <p><span style="display:inline-block;">"""
            + _(
                "This website is NOT affiliated with or endorsed by Winterpixel Games Inc."
            )
            + """</span><span style="display:inline-block;">&nbsp;"""
            + _("All relevant trademarks belong to their respective owners.")
            + """</span><br>"""
            + _(
                'Developed with 💖 by <a style="text-decoration:none" href="https://tank8k.com/" target="_blank">TANK8K</a>'
            )
            + """</p>
            <style>
            div[data-testid="stSidebarContent"] button p::before {
                font-family: "Font Awesome 5 Free" !important;
                display: inline-block;
                vertical-align: middle;
                font-weight: 800;
                font-size: 20px;
                color: white;
                min-width: 35px;
                padding-right: 7px;
            }
            div[data-testid="stSidebarContent"] button p::after {
                font-family: 'Baloo 2';
                font-weight: 700;
                font-size: 20px;
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(3) {
                position: relative;
                bottom: 15px;
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(3) div[data-testid="column"]:nth-child(1) button[data-testid="baseButton-primary"] p::before {
                content: "\\f52b";
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(3) div[data-testid="column"]:nth-child(1) button[data-testid="baseButton-primary"] p::after {
                content: '"""
            + _("Log Out")
            + """';
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(3) div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-primary"] p::before {
                content: "\\f2bb";
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(3) div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-primary"] p::after {
                content: '"""
            + _("Account")
            + """';
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(2) div[data-testid="column"]:nth-child(1) button[data-testid="baseButton-primary"] p::before {
                content: "\\f2f6";
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(2) div[data-testid="column"]:nth-child(1) button[data-testid="baseButton-primary"] p::after {
                content: '"""
            + _("Log In")
            + """';
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(2) div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-primary"] p::before {
                content: "\\f234";
            }
            div[data-testid="stSidebarContent"] div[data-testid="stHorizontalBlock"]:nth-child(2) div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-primary"] p::after {
                content: '"""
            + _("Sign Up")
            + """';
            }
            div[data-testid="stSidebarContent"] button[data-testid="baseButton-secondary"] p::before {
                content: "\\f1ab";
            }
            div[data-testid="stSidebarContent"] button[data-testid="baseButton-secondary"] p::after {
                content: '"""
            + _("Language")
            + """';
            }
            div[data-testid="stSidebarContent"] div[data-testid="stVerticalBlock"] div[data-testid="element-container"]:nth-child(2) button[data-testid="baseButton-primary"] p::after {
                content: '"""
            + _("Log Out")
            + """';
            }
            div[data-testid="stSidebarContent"] div[data-testid="stVerticalBlock"] div[data-testid="element-container"]:nth-child(2) button[data-testid="baseButton-primary"] p::before {
                content: "\\f52b";
            }
            div[role="dialog"] div[data-testid="stLinkButton"] > a[kind="primary"]::before{
                font-family: "Font Awesome 5 Free" !important;
                content: "\\f2b5";
                display: inline-block;
                vertical-align: middle;
                font-weight: 800;
                font-size: 18px;
                color: white;
                min-width: 35px;
                padding-left: 7px;
            }
            div[role="dialog"] div[data-testid="stLinkButton"] button p, div[role="dialog"] div[data-testid="stLinkButton"] a p  {
                font-family: 'Baloo 2';
                font-weight: 700;
                font-size: 18px;
            }
            div[role="dialog"] div[data-testid="stExpander"] a {
                border: none;
                box-shadow: none;
                background: transparent;
                color: white;
                padding: 0;
                margin: 0;
            }
            div[role="dialog"] div[data-testid="stExpander"] p {
                font-family: 'Baloo 2' !impotant;
                font-weight: 700 !important;
                font-size: 18px !important;
            }
            div[role="dialog"] div[data-testid="stExpander"] .row-widget.stLinkButton p::after {
                font-family: "Font Awesome 5 Free" !important;
                content: "\\f0c1";
                display: inline-block;
                vertical-align: middle;
                font-weight: 800;
                font-size: 15px;
                color: white;
                min-width: 35px;
                padding-left: 7px;
            }
            div[role="dialog"] div[data-testid="stExpander"] a:hover {
                border: none;
                box-shadow: none;
                background: transparent;
                color: rgb(48, 151, 230);
                text-decoration: underline !important;
            }
            div[role="dialog"] div[data-testid="stExpander"] .row-widget.stLinkButton {
                height: 18px;
            }
            div[role="dialog"] button[data-testid="baseButton-secondary"]::before {
                font-family: "Font Awesome 5 Free" !important;
                content: "\\f058";
                display: inline-block;
                vertical-align: middle;
                font-weight: 800;
                font-size: 18px;
                color: white;
                padding-right: 7px;
            }
            div[data-testid="stExpanderDetails"] .row-widget.stLinkButton::before {
                content: "- ";
            }
            div[role="dialog"] div[data-testid="stVerticalBlock"] > div[data-testid="element-container"]:nth-child(3) {
                #display: none;
            }
            div[data-testid="stExpanderDetails"] div[data-testid="element-container"]:nth-child(3) {
                display: contents !important;
            }
        }
            </style>
        </div>
    """
        ),
        unsafe_allow_html=True,
    )
