
don't allow old protocols

conditional access policies

geographic locations

blocking legacy auth

force compliant devices


https://github.com/BitLyft/IOCs

## intune

```
 I deploy the following policies at a minimum, I bolded the policies specifically aimed at devices.

    Block basic authentication.

    Block access unless it's from a country listed in a Named Location list.

    Restrict Service Accounts to specified Named Locations list(s).

    Block access to unsupported devices (anything other than iOS, Android, Windows, and macOS).

    Restrict Guest Access to Office 365, Microsoft Azure Information Protection, and My Apps.

    Require Terms of Use acceptance.

    Block Unmanaged File downloads.

    Require MDM or MAM for iOS and Android devices.

    Require MFA for all admin roles with daily sign-in frequency.

    Require MFA for all users with a 60-day sign-in frequency.

    Require MFA for all guests with a 7-day sign-in frequency.

When possible, I implement the following. However, this can vary based on client variables.

    Require MDM for Windows or macOS devices.

The following are added if AAD P2 is available:

    Block High Sign-In Risk.

    Block High User Risk.

    Require MFA for Low or Medium Sign-In Risk.

    Require MFA for Low or Medium User Risk.

    Create a Break Glass account, named as innocuously as possible, so as to hide in plain sight.

        Set per-user MFA on it, and ensure you keep the password long and in some secure password management system like BitWarden.

        Keep the TOTP or Authenticator code in a separate system.

    Add the Break Glass account to be excluded from every single policy before you turn on the policy.

```

https://danielchronlund.com/2020/11/26/azure-ad-conditional-access-policy-design-baseline-with-automatic-deployment-support/
https://www.vansurksum.com/2022/12/15/december-2022-update-of-the-conditional-access-demystified-whitepaper-and-workflow-cheat-sheet/
