/* 
 * BtcTurk API 3.0
 *
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// WithdrawalCommissionsModel
    /// </summary>
    [DataContract]
        public partial class WithdrawalCommissionsModel :  IEquatable<WithdrawalCommissionsModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="WithdrawalCommissionsModel" /> class.
        /// </summary>
        /// <param name="cryptoChannelName">cryptoChannelName.</param>
        /// <param name="commissionType">commissionType.</param>
        /// <param name="currencyPrecision">currencyPrecision.</param>
        /// <param name="feeValue">feeValue.</param>
        public WithdrawalCommissionsModel(string cryptoChannelName = default(string), CommissionType commissionType = default(CommissionType), int? currencyPrecision = default(int?), double? feeValue = default(double?))
        {
            this.CryptoChannelName = cryptoChannelName;
            this.CommissionType = commissionType;
            this.CurrencyPrecision = currencyPrecision;
            this.FeeValue = feeValue;
        }
        
        /// <summary>
        /// Gets or Sets CryptoChannelName
        /// </summary>
        [DataMember(Name="cryptoChannelName", EmitDefaultValue=false)]
        public string CryptoChannelName { get; set; }

        /// <summary>
        /// Gets or Sets CommissionType
        /// </summary>
        [DataMember(Name="commissionType", EmitDefaultValue=false)]
        public CommissionType CommissionType { get; set; }

        /// <summary>
        /// Gets or Sets CurrencyPrecision
        /// </summary>
        [DataMember(Name="currencyPrecision", EmitDefaultValue=false)]
        public int? CurrencyPrecision { get; set; }

        /// <summary>
        /// Gets or Sets FeeValue
        /// </summary>
        [DataMember(Name="feeValue", EmitDefaultValue=false)]
        public double? FeeValue { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class WithdrawalCommissionsModel {\n");
            sb.Append("  CryptoChannelName: ").Append(CryptoChannelName).Append("\n");
            sb.Append("  CommissionType: ").Append(CommissionType).Append("\n");
            sb.Append("  CurrencyPrecision: ").Append(CurrencyPrecision).Append("\n");
            sb.Append("  FeeValue: ").Append(FeeValue).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as WithdrawalCommissionsModel);
        }

        /// <summary>
        /// Returns true if WithdrawalCommissionsModel instances are equal
        /// </summary>
        /// <param name="input">Instance of WithdrawalCommissionsModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(WithdrawalCommissionsModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.CryptoChannelName == input.CryptoChannelName ||
                    (this.CryptoChannelName != null &&
                    this.CryptoChannelName.Equals(input.CryptoChannelName))
                ) && 
                (
                    this.CommissionType == input.CommissionType ||
                    (this.CommissionType != null &&
                    this.CommissionType.Equals(input.CommissionType))
                ) && 
                (
                    this.CurrencyPrecision == input.CurrencyPrecision ||
                    (this.CurrencyPrecision != null &&
                    this.CurrencyPrecision.Equals(input.CurrencyPrecision))
                ) && 
                (
                    this.FeeValue == input.FeeValue ||
                    (this.FeeValue != null &&
                    this.FeeValue.Equals(input.FeeValue))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.CryptoChannelName != null)
                    hashCode = hashCode * 59 + this.CryptoChannelName.GetHashCode();
                if (this.CommissionType != null)
                    hashCode = hashCode * 59 + this.CommissionType.GetHashCode();
                if (this.CurrencyPrecision != null)
                    hashCode = hashCode * 59 + this.CurrencyPrecision.GetHashCode();
                if (this.FeeValue != null)
                    hashCode = hashCode * 59 + this.FeeValue.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}