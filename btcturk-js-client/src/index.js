/*
 * BtcTurk API 3.0
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.34
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from './ApiClient';
import {AccountAddressModel} from './model/AccountAddressModel';
import {AkbankDirektCommissionOutputModel} from './model/AkbankDirektCommissionOutputModel';
import {AkbankDirektLimit} from './model/AkbankDirektLimit';
import {AlarmInterval} from './model/AlarmInterval';
import {AlarmTypes} from './model/AlarmTypes';
import {AlarmVector} from './model/AlarmVector';
import {AnnouncementDetailModel} from './model/AnnouncementDetailModel';
import {AnnouncementDetailModelIPagedList} from './model/AnnouncementDetailModelIPagedList';
import {AnnouncementModel} from './model/AnnouncementModel';
import {AnnouncementModelIPagedList} from './model/AnnouncementModelIPagedList';
import {AppRatingEnum} from './model/AppRatingEnum';
import {AppRatingRequestModel} from './model/AppRatingRequestModel';
import {BadRequestErrorModel} from './model/BadRequestErrorModel';
import {BadRequestResponseModel} from './model/BadRequestResponseModel';
import {BankCommissionOutputModel} from './model/BankCommissionOutputModel';
import {BankLimit} from './model/BankLimit';
import {BugBountyNoticeRequestModel} from './model/BugBountyNoticeRequestModel';
import {CardRegistrationRequestViewModel} from './model/CardRegistrationRequestViewModel';
import {CheckCurrencyRiskAgreementResponseModel} from './model/CheckCurrencyRiskAgreementResponseModel';
import {CheckPairRiskAgreementResponseModel} from './model/CheckPairRiskAgreementResponseModel';
import {CommissionOutputModel} from './model/CommissionOutputModel';
import {CommissionType} from './model/CommissionType';
import {CreateAlarmRequest} from './model/CreateAlarmRequest';
import {CreateSplashScreenLoginRequestModel} from './model/CreateSplashScreenLoginRequestModel';
import {CryptoCommissionOutputModel} from './model/CryptoCommissionOutputModel';
import {CryptoCurrencySymbol} from './model/CryptoCurrencySymbol';
import {CryptoWithdrawValidationResponseModel} from './model/CryptoWithdrawValidationResponseModel';
import {CryptoWithdrawalCommissionsResponseModel} from './model/CryptoWithdrawalCommissionsResponseModel';
import {CryptoWithdrawalDeleteInputModel} from './model/CryptoWithdrawalDeleteInputModel';
import {CurrencyLimit} from './model/CurrencyLimit';
import {CurrencyTransferType} from './model/CurrencyTransferType';
import {CurrencyType} from './model/CurrencyType';
import {DocumentFileType} from './model/DocumentFileType';
import {FiatDepositBankAccountModel} from './model/FiatDepositBankAccountModel';
import {HallOfFrameResponseModel} from './model/HallOfFrameResponseModel';
import {JumioKycIdentityVerificationRequestModel} from './model/JumioKycIdentityVerificationRequestModel';
import {LanguageInfoModel} from './model/LanguageInfoModel';
import {LanguageSettingModel} from './model/LanguageSettingModel';
import {LevelLimitValues} from './model/LevelLimitValues';
import {LevelLimits} from './model/LevelLimits';
import {LimitOutputModel} from './model/LimitOutputModel';
import {LimitType} from './model/LimitType';
import {MobileSettingModel} from './model/MobileSettingModel';
import {MobilejwtPlatformBody} from './model/MobilejwtPlatformBody';
import {NotificationShowType} from './model/NotificationShowType';
import {OrderMethod} from './model/OrderMethod';
import {PairLimit} from './model/PairLimit';
import {PaparaCommissionOutputModel} from './model/PaparaCommissionOutputModel';
import {PaparaLimit} from './model/PaparaLimit';
import {ProblemDetails} from './model/ProblemDetails';
import {ReportDepositWithdrawalInputModel} from './model/ReportDepositWithdrawalInputModel';
import {ReportTradeHistoryInputModel} from './model/ReportTradeHistoryInputModel';
import {ReportTransactionHistoryInputModel} from './model/ReportTransactionHistoryInputModel';
import {ReturnCodeType} from './model/ReturnCodeType';
import {ReturnModel} from './model/ReturnModel';
import {SplashScreenLoginType} from './model/SplashScreenLoginType';
import {SystemNotificationContentModel} from './model/SystemNotificationContentModel';
import {SystemNotificationCountModel} from './model/SystemNotificationCountModel';
import {SystemNotificationModel} from './model/SystemNotificationModel';
import {SystemNotificationModelIPagedList} from './model/SystemNotificationModelIPagedList';
import {SystemNotificationReadModel} from './model/SystemNotificationReadModel';
import {SystemNotificationRequestType} from './model/SystemNotificationRequestType';
import {UserAgreementApproveModel} from './model/UserAgreementApproveModel';
import {UserAgreementModel} from './model/UserAgreementModel';
import {UserAllLimitsModel} from './model/UserAllLimitsModel';
import {UserDonationRequestModel} from './model/UserDonationRequestModel';
import {UserTradeFeeRateErrorModel} from './model/UserTradeFeeRateErrorModel';
import {UserTradeFeeRateOutputModel} from './model/UserTradeFeeRateOutputModel';
import {WithdrawalCommissionsModel} from './model/WithdrawalCommissionsModel';
import {AccountApi} from './api/AccountApi';
import {AlarmApi} from './api/AlarmApi';
import {BugBountyApi} from './api/BugBountyApi';
import {CardRegistrationApi} from './api/CardRegistrationApi';
import {CryptoDepositApi} from './api/CryptoDepositApi';
import {CryptoWithdrawApi} from './api/CryptoWithdrawApi';
import {CryptoWithdrawalCommissionsApi} from './api/CryptoWithdrawalCommissionsApi';
import {ExchangeApi} from './api/ExchangeApi';
import {FeedbackApi} from './api/FeedbackApi';
import {FiatDepositApi} from './api/FiatDepositApi';
import {FiatWithdrawalCommissionsApi} from './api/FiatWithdrawalCommissionsApi';
import {HalvingApi} from './api/HalvingApi';
import {HelpApi} from './api/HelpApi';
import {HomeApi} from './api/HomeApi';
import {KnowYourCustomerApi} from './api/KnowYourCustomerApi';
import {MobileApi} from './api/MobileApi';
import {NotificationApi} from './api/NotificationApi';
import {RemainderApi} from './api/RemainderApi';
import {ReportApi} from './api/ReportApi';
import {SupportPlatformsApi} from './api/SupportPlatformsApi';
import {UserAgreementApi} from './api/UserAgreementApi';
import {UserDeviceApi} from './api/UserDeviceApi';
import {UserDonationApi} from './api/UserDonationApi';

/**
* White_label_exchange_API_documentation_.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var BtcTurkAp30 = require('index'); // See note below*.
* var xxxSvc = new BtcTurkAp30.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new BtcTurkAp30.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new BtcTurkAp30.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new BtcTurkAp30.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 3.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AccountAddressModel model constructor.
     * @property {module:model/AccountAddressModel}
     */
    AccountAddressModel,

    /**
     * The AkbankDirektCommissionOutputModel model constructor.
     * @property {module:model/AkbankDirektCommissionOutputModel}
     */
    AkbankDirektCommissionOutputModel,

    /**
     * The AkbankDirektLimit model constructor.
     * @property {module:model/AkbankDirektLimit}
     */
    AkbankDirektLimit,

    /**
     * The AlarmInterval model constructor.
     * @property {module:model/AlarmInterval}
     */
    AlarmInterval,

    /**
     * The AlarmTypes model constructor.
     * @property {module:model/AlarmTypes}
     */
    AlarmTypes,

    /**
     * The AlarmVector model constructor.
     * @property {module:model/AlarmVector}
     */
    AlarmVector,

    /**
     * The AnnouncementDetailModel model constructor.
     * @property {module:model/AnnouncementDetailModel}
     */
    AnnouncementDetailModel,

    /**
     * The AnnouncementDetailModelIPagedList model constructor.
     * @property {module:model/AnnouncementDetailModelIPagedList}
     */
    AnnouncementDetailModelIPagedList,

    /**
     * The AnnouncementModel model constructor.
     * @property {module:model/AnnouncementModel}
     */
    AnnouncementModel,

    /**
     * The AnnouncementModelIPagedList model constructor.
     * @property {module:model/AnnouncementModelIPagedList}
     */
    AnnouncementModelIPagedList,

    /**
     * The AppRatingEnum model constructor.
     * @property {module:model/AppRatingEnum}
     */
    AppRatingEnum,

    /**
     * The AppRatingRequestModel model constructor.
     * @property {module:model/AppRatingRequestModel}
     */
    AppRatingRequestModel,

    /**
     * The BadRequestErrorModel model constructor.
     * @property {module:model/BadRequestErrorModel}
     */
    BadRequestErrorModel,

    /**
     * The BadRequestResponseModel model constructor.
     * @property {module:model/BadRequestResponseModel}
     */
    BadRequestResponseModel,

    /**
     * The BankCommissionOutputModel model constructor.
     * @property {module:model/BankCommissionOutputModel}
     */
    BankCommissionOutputModel,

    /**
     * The BankLimit model constructor.
     * @property {module:model/BankLimit}
     */
    BankLimit,

    /**
     * The BugBountyNoticeRequestModel model constructor.
     * @property {module:model/BugBountyNoticeRequestModel}
     */
    BugBountyNoticeRequestModel,

    /**
     * The CardRegistrationRequestViewModel model constructor.
     * @property {module:model/CardRegistrationRequestViewModel}
     */
    CardRegistrationRequestViewModel,

    /**
     * The CheckCurrencyRiskAgreementResponseModel model constructor.
     * @property {module:model/CheckCurrencyRiskAgreementResponseModel}
     */
    CheckCurrencyRiskAgreementResponseModel,

    /**
     * The CheckPairRiskAgreementResponseModel model constructor.
     * @property {module:model/CheckPairRiskAgreementResponseModel}
     */
    CheckPairRiskAgreementResponseModel,

    /**
     * The CommissionOutputModel model constructor.
     * @property {module:model/CommissionOutputModel}
     */
    CommissionOutputModel,

    /**
     * The CommissionType model constructor.
     * @property {module:model/CommissionType}
     */
    CommissionType,

    /**
     * The CreateAlarmRequest model constructor.
     * @property {module:model/CreateAlarmRequest}
     */
    CreateAlarmRequest,

    /**
     * The CreateSplashScreenLoginRequestModel model constructor.
     * @property {module:model/CreateSplashScreenLoginRequestModel}
     */
    CreateSplashScreenLoginRequestModel,

    /**
     * The CryptoCommissionOutputModel model constructor.
     * @property {module:model/CryptoCommissionOutputModel}
     */
    CryptoCommissionOutputModel,

    /**
     * The CryptoCurrencySymbol model constructor.
     * @property {module:model/CryptoCurrencySymbol}
     */
    CryptoCurrencySymbol,

    /**
     * The CryptoWithdrawValidationResponseModel model constructor.
     * @property {module:model/CryptoWithdrawValidationResponseModel}
     */
    CryptoWithdrawValidationResponseModel,

    /**
     * The CryptoWithdrawalCommissionsResponseModel model constructor.
     * @property {module:model/CryptoWithdrawalCommissionsResponseModel}
     */
    CryptoWithdrawalCommissionsResponseModel,

    /**
     * The CryptoWithdrawalDeleteInputModel model constructor.
     * @property {module:model/CryptoWithdrawalDeleteInputModel}
     */
    CryptoWithdrawalDeleteInputModel,

    /**
     * The CurrencyLimit model constructor.
     * @property {module:model/CurrencyLimit}
     */
    CurrencyLimit,

    /**
     * The CurrencyTransferType model constructor.
     * @property {module:model/CurrencyTransferType}
     */
    CurrencyTransferType,

    /**
     * The CurrencyType model constructor.
     * @property {module:model/CurrencyType}
     */
    CurrencyType,

    /**
     * The DocumentFileType model constructor.
     * @property {module:model/DocumentFileType}
     */
    DocumentFileType,

    /**
     * The FiatDepositBankAccountModel model constructor.
     * @property {module:model/FiatDepositBankAccountModel}
     */
    FiatDepositBankAccountModel,

    /**
     * The HallOfFrameResponseModel model constructor.
     * @property {module:model/HallOfFrameResponseModel}
     */
    HallOfFrameResponseModel,

    /**
     * The JumioKycIdentityVerificationRequestModel model constructor.
     * @property {module:model/JumioKycIdentityVerificationRequestModel}
     */
    JumioKycIdentityVerificationRequestModel,

    /**
     * The LanguageInfoModel model constructor.
     * @property {module:model/LanguageInfoModel}
     */
    LanguageInfoModel,

    /**
     * The LanguageSettingModel model constructor.
     * @property {module:model/LanguageSettingModel}
     */
    LanguageSettingModel,

    /**
     * The LevelLimitValues model constructor.
     * @property {module:model/LevelLimitValues}
     */
    LevelLimitValues,

    /**
     * The LevelLimits model constructor.
     * @property {module:model/LevelLimits}
     */
    LevelLimits,

    /**
     * The LimitOutputModel model constructor.
     * @property {module:model/LimitOutputModel}
     */
    LimitOutputModel,

    /**
     * The LimitType model constructor.
     * @property {module:model/LimitType}
     */
    LimitType,

    /**
     * The MobileSettingModel model constructor.
     * @property {module:model/MobileSettingModel}
     */
    MobileSettingModel,

    /**
     * The MobilejwtPlatformBody model constructor.
     * @property {module:model/MobilejwtPlatformBody}
     */
    MobilejwtPlatformBody,

    /**
     * The NotificationShowType model constructor.
     * @property {module:model/NotificationShowType}
     */
    NotificationShowType,

    /**
     * The OrderMethod model constructor.
     * @property {module:model/OrderMethod}
     */
    OrderMethod,

    /**
     * The PairLimit model constructor.
     * @property {module:model/PairLimit}
     */
    PairLimit,

    /**
     * The PaparaCommissionOutputModel model constructor.
     * @property {module:model/PaparaCommissionOutputModel}
     */
    PaparaCommissionOutputModel,

    /**
     * The PaparaLimit model constructor.
     * @property {module:model/PaparaLimit}
     */
    PaparaLimit,

    /**
     * The ProblemDetails model constructor.
     * @property {module:model/ProblemDetails}
     */
    ProblemDetails,

    /**
     * The ReportDepositWithdrawalInputModel model constructor.
     * @property {module:model/ReportDepositWithdrawalInputModel}
     */
    ReportDepositWithdrawalInputModel,

    /**
     * The ReportTradeHistoryInputModel model constructor.
     * @property {module:model/ReportTradeHistoryInputModel}
     */
    ReportTradeHistoryInputModel,

    /**
     * The ReportTransactionHistoryInputModel model constructor.
     * @property {module:model/ReportTransactionHistoryInputModel}
     */
    ReportTransactionHistoryInputModel,

    /**
     * The ReturnCodeType model constructor.
     * @property {module:model/ReturnCodeType}
     */
    ReturnCodeType,

    /**
     * The ReturnModel model constructor.
     * @property {module:model/ReturnModel}
     */
    ReturnModel,

    /**
     * The SplashScreenLoginType model constructor.
     * @property {module:model/SplashScreenLoginType}
     */
    SplashScreenLoginType,

    /**
     * The SystemNotificationContentModel model constructor.
     * @property {module:model/SystemNotificationContentModel}
     */
    SystemNotificationContentModel,

    /**
     * The SystemNotificationCountModel model constructor.
     * @property {module:model/SystemNotificationCountModel}
     */
    SystemNotificationCountModel,

    /**
     * The SystemNotificationModel model constructor.
     * @property {module:model/SystemNotificationModel}
     */
    SystemNotificationModel,

    /**
     * The SystemNotificationModelIPagedList model constructor.
     * @property {module:model/SystemNotificationModelIPagedList}
     */
    SystemNotificationModelIPagedList,

    /**
     * The SystemNotificationReadModel model constructor.
     * @property {module:model/SystemNotificationReadModel}
     */
    SystemNotificationReadModel,

    /**
     * The SystemNotificationRequestType model constructor.
     * @property {module:model/SystemNotificationRequestType}
     */
    SystemNotificationRequestType,

    /**
     * The UserAgreementApproveModel model constructor.
     * @property {module:model/UserAgreementApproveModel}
     */
    UserAgreementApproveModel,

    /**
     * The UserAgreementModel model constructor.
     * @property {module:model/UserAgreementModel}
     */
    UserAgreementModel,

    /**
     * The UserAllLimitsModel model constructor.
     * @property {module:model/UserAllLimitsModel}
     */
    UserAllLimitsModel,

    /**
     * The UserDonationRequestModel model constructor.
     * @property {module:model/UserDonationRequestModel}
     */
    UserDonationRequestModel,

    /**
     * The UserTradeFeeRateErrorModel model constructor.
     * @property {module:model/UserTradeFeeRateErrorModel}
     */
    UserTradeFeeRateErrorModel,

    /**
     * The UserTradeFeeRateOutputModel model constructor.
     * @property {module:model/UserTradeFeeRateOutputModel}
     */
    UserTradeFeeRateOutputModel,

    /**
     * The WithdrawalCommissionsModel model constructor.
     * @property {module:model/WithdrawalCommissionsModel}
     */
    WithdrawalCommissionsModel,

    /**
    * The AccountApi service constructor.
    * @property {module:api/AccountApi}
    */
    AccountApi,

    /**
    * The AlarmApi service constructor.
    * @property {module:api/AlarmApi}
    */
    AlarmApi,

    /**
    * The BugBountyApi service constructor.
    * @property {module:api/BugBountyApi}
    */
    BugBountyApi,

    /**
    * The CardRegistrationApi service constructor.
    * @property {module:api/CardRegistrationApi}
    */
    CardRegistrationApi,

    /**
    * The CryptoDepositApi service constructor.
    * @property {module:api/CryptoDepositApi}
    */
    CryptoDepositApi,

    /**
    * The CryptoWithdrawApi service constructor.
    * @property {module:api/CryptoWithdrawApi}
    */
    CryptoWithdrawApi,

    /**
    * The CryptoWithdrawalCommissionsApi service constructor.
    * @property {module:api/CryptoWithdrawalCommissionsApi}
    */
    CryptoWithdrawalCommissionsApi,

    /**
    * The ExchangeApi service constructor.
    * @property {module:api/ExchangeApi}
    */
    ExchangeApi,

    /**
    * The FeedbackApi service constructor.
    * @property {module:api/FeedbackApi}
    */
    FeedbackApi,

    /**
    * The FiatDepositApi service constructor.
    * @property {module:api/FiatDepositApi}
    */
    FiatDepositApi,

    /**
    * The FiatWithdrawalCommissionsApi service constructor.
    * @property {module:api/FiatWithdrawalCommissionsApi}
    */
    FiatWithdrawalCommissionsApi,

    /**
    * The HalvingApi service constructor.
    * @property {module:api/HalvingApi}
    */
    HalvingApi,

    /**
    * The HelpApi service constructor.
    * @property {module:api/HelpApi}
    */
    HelpApi,

    /**
    * The HomeApi service constructor.
    * @property {module:api/HomeApi}
    */
    HomeApi,

    /**
    * The KnowYourCustomerApi service constructor.
    * @property {module:api/KnowYourCustomerApi}
    */
    KnowYourCustomerApi,

    /**
    * The MobileApi service constructor.
    * @property {module:api/MobileApi}
    */
    MobileApi,

    /**
    * The NotificationApi service constructor.
    * @property {module:api/NotificationApi}
    */
    NotificationApi,

    /**
    * The RemainderApi service constructor.
    * @property {module:api/RemainderApi}
    */
    RemainderApi,

    /**
    * The ReportApi service constructor.
    * @property {module:api/ReportApi}
    */
    ReportApi,

    /**
    * The SupportPlatformsApi service constructor.
    * @property {module:api/SupportPlatformsApi}
    */
    SupportPlatformsApi,

    /**
    * The UserAgreementApi service constructor.
    * @property {module:api/UserAgreementApi}
    */
    UserAgreementApi,

    /**
    * The UserDeviceApi service constructor.
    * @property {module:api/UserDeviceApi}
    */
    UserDeviceApi,

    /**
    * The UserDonationApi service constructor.
    * @property {module:api/UserDonationApi}
    */
    UserDonationApi
};