/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */

import { action } from 'typesafe-actions'

// Constant
import { types } from '../constants/rewards_types'

export const createWallet = () => action(types.CREATE_WALLET)

export const onWalletCreated = () => action(types.WALLET_CREATED)

export const onWalletCreateFailed = () => action(types.WALLET_CREATE_FAILED)

export const onSettingSave = (key: string, value: any) => action(types.ON_SETTING_SAVE, {
  key,
  value
})

export const getWalletProperties = () => action(types.GET_WALLET_PROPERTIES)

export const onWalletProperties = (properties: {status: number, wallet: Rewards.WalletProperties, monthlyAmount: number}) =>
  action(types.ON_WALLET_PROPERTIES, {
    properties
  })

export const getGrants = () => action(types.GET_GRANTS)

export const onGrant = (properties: Rewards.GrantResponse) => action(types.ON_GRANT, {
  properties
})

export const getGrantCaptcha = (promotionId?: string) => action(types.GET_GRANT_CAPTCHA, {
  promotionId
})

export const onGrantCaptcha = (captcha: Rewards.Captcha) => action(types.ON_GRANT_CAPTCHA, {
  captcha
})

export const solveGrantCaptcha = (x: number, y: number) => action(types.SOLVE_GRANT_CAPTCHA, {
  x,
  y
})

export const onGrantFinish = (properties: Rewards.GrantFinish) => action(types.ON_GRANT_FINISH, {
  properties
})

export const onResetGrant = () => action(types.ON_GRANT_RESET)

export const onDeleteGrant = () => action(types.ON_GRANT_DELETE)

export const getWalletPassphrase = () => action(types.GET_WALLLET_PASSPHRASE)

export const onWalletPassphrase = (pass: string) => action(types.ON_WALLLET_PASSPHRASE, {
  pass
})

export const recoverWallet = (key: string) => action(types.RECOVER_WALLET, {
  key
})

export const onRecoverWalletData = (properties: Rewards.RecoverWallet) => action(types.ON_RECOVER_WALLET_DATA, {
  properties
})

export const onModalBackupClose = () => action(types.ON_MODAL_BACKUP_CLOSE)

export const onModalBackupOpen = () => action(types.ON_MODAL_BACKUP_OPEN)

export const onClearAlert = (property: string) => action(types.ON_CLEAR_ALERT, {
  property
})

export const onReconcileStamp = (stamp: number) => action(types.ON_RECONCILE_STAMP, {
  stamp
})

export const onAddresses = (addresses: Record<string, string>) => action(types.ON_ADDRESSES, {
  addresses
})

export const onQRGenerated = (type: Rewards.AddressesType, image: string) => action(types.ON_QR_GENERATED, {
  type,
  image
})

export const getContributeList = () => action(types.GET_CONTRIBUTE_LIST)

export const onContributeList = (list: Rewards.Publisher[]) => action(types.ON_CONTRIBUTE_LIST, {
  list
})

export const getCurrentReport = () => action(types.GET_CURRENT_REPORT, {})

export const onBalanceReports = (reports: Record<string, Rewards.Report>) => action(types.ON_BALANCE_REPORTS, {
  reports
})

export const excludePublisher = (publisherKey: string) => action(types.ON_EXCLUDE_PUBLISHER, {
  publisherKey
})

export const checkWalletExistence = () => action(types.CHECK_WALLET_EXISTENCE)

export const onWalletExists = (exists: boolean) => action(types.ON_WALLET_EXISTS, {
  exists
})

export const restorePublishers = () => action(types.ON_RESTORE_PUBLISHERS)

export const onNumExcludedSites = (excludedSitesInfo: {num: string, publisherKey: string}) => action(types.ON_NUM_EXCLUDED_SITES, {
  excludedSitesInfo
})

export const onExcludedNumber = (num: number) => action(types.ON_EXCLUDED_PUBLISHERS_NUMBER, {
  num
})

export const onContributionAmount = (amount: number) => action(types.ON_CONTRIBUTION_AMOUNT, {
  amount
})

export const getAdsData = () => action(types.GET_ADS_DATA)

export const onAdsData = (adsData: Rewards.AdsData) => action(types.ON_ADS_DATA, {
  adsData
})

export const onAdsSettingSave = (key: string, value: any) => action(types.ON_ADS_SETTING_SAVE, {
  key,
  value
})

export const onTransactionHistory = (data: {adsEstimatedPendingRewards: number, adsNextPaymentDate: string, adsNotificationsReceivedThisMonth: number}) =>
  action(types.ON_TRANSACTION_HISTORY, {
    data
  })

export const getTransactionHistory = () => action(types.GET_TRANSACTION_HISTORY)

export const onTransactionHistoryChanged = () => action(types.ON_TRANSACTION_HISTORY_CHANGED)

export const onInitAutoContributeSettings = (properties: any) => action(types.INIT_AUTOCONTRIBUTE_SETTINGS, {
  properties
})

export const getDonationTable = () => action(types.GET_DONATION_TABLE)

export const onRecurringDonationUpdate = (list: Rewards.Publisher[]) => action(types.ON_RECURRING_DONATION_UPDATE, {
  list
})

export const onCurrentTips = (list: Rewards.Publisher[]) => action(types.ON_CURRENT_TIPS, {
  list
})

export const removeRecurring = (publisherKey: string) => action(types.ON_REMOVE_RECURRING, {
  publisherKey
})

export const getRewardsEnabled = () => action(types.GET_REWARDS_ENABLED)

export const onRewardsEnabled = (enabled: boolean) => action(types.ON_REWARDS_ENABLED, {
  enabled
})

export const getPendingContributionsTotal = () => action(types.GET_PENDING_CONTRIBUTION_TOTAL)

export const onPendingContributionTotal = (amount: number) => action(types.ON_PENDING_CONTRIBUTION_TOTAL, {
  amount
})

export const onRecurringTipRemoved = (success: boolean) => action(types.ON_RECURRING_TIP_REMOVED, {
  success
})

export const getExcludedPublishersNumber = () => action(types.GET_EXCLUDED_PUBLISHERS_NUMBER)
