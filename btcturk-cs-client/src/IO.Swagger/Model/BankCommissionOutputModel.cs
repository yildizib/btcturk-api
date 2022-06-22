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
    /// BankCommissionOutputModel
    /// </summary>
    [DataContract]
        public partial class BankCommissionOutputModel :  IEquatable<BankCommissionOutputModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="BankCommissionOutputModel" /> class.
        /// </summary>
        /// <param name="depositFee">depositFee.</param>
        /// <param name="withdrawalFee">withdrawalFee.</param>
        /// <param name="depositTax">depositTax.</param>
        /// <param name="withdrawalTax">withdrawalTax.</param>
        /// <param name="currency">currency.</param>
        public BankCommissionOutputModel(double? depositFee = default(double?), double? withdrawalFee = default(double?), double? depositTax = default(double?), double? withdrawalTax = default(double?), string currency = default(string))
        {
            this.DepositFee = depositFee;
            this.WithdrawalFee = withdrawalFee;
            this.DepositTax = depositTax;
            this.WithdrawalTax = withdrawalTax;
            this.Currency = currency;
        }
        
        /// <summary>
        /// Gets or Sets DepositFee
        /// </summary>
        [DataMember(Name="depositFee", EmitDefaultValue=false)]
        public double? DepositFee { get; set; }

        /// <summary>
        /// Gets or Sets WithdrawalFee
        /// </summary>
        [DataMember(Name="withdrawalFee", EmitDefaultValue=false)]
        public double? WithdrawalFee { get; set; }

        /// <summary>
        /// Gets or Sets DepositTax
        /// </summary>
        [DataMember(Name="depositTax", EmitDefaultValue=false)]
        public double? DepositTax { get; set; }

        /// <summary>
        /// Gets or Sets WithdrawalTax
        /// </summary>
        [DataMember(Name="withdrawalTax", EmitDefaultValue=false)]
        public double? WithdrawalTax { get; set; }

        /// <summary>
        /// Gets or Sets Currency
        /// </summary>
        [DataMember(Name="currency", EmitDefaultValue=false)]
        public string Currency { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class BankCommissionOutputModel {\n");
            sb.Append("  DepositFee: ").Append(DepositFee).Append("\n");
            sb.Append("  WithdrawalFee: ").Append(WithdrawalFee).Append("\n");
            sb.Append("  DepositTax: ").Append(DepositTax).Append("\n");
            sb.Append("  WithdrawalTax: ").Append(WithdrawalTax).Append("\n");
            sb.Append("  Currency: ").Append(Currency).Append("\n");
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
            return this.Equals(input as BankCommissionOutputModel);
        }

        /// <summary>
        /// Returns true if BankCommissionOutputModel instances are equal
        /// </summary>
        /// <param name="input">Instance of BankCommissionOutputModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(BankCommissionOutputModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.DepositFee == input.DepositFee ||
                    (this.DepositFee != null &&
                    this.DepositFee.Equals(input.DepositFee))
                ) && 
                (
                    this.WithdrawalFee == input.WithdrawalFee ||
                    (this.WithdrawalFee != null &&
                    this.WithdrawalFee.Equals(input.WithdrawalFee))
                ) && 
                (
                    this.DepositTax == input.DepositTax ||
                    (this.DepositTax != null &&
                    this.DepositTax.Equals(input.DepositTax))
                ) && 
                (
                    this.WithdrawalTax == input.WithdrawalTax ||
                    (this.WithdrawalTax != null &&
                    this.WithdrawalTax.Equals(input.WithdrawalTax))
                ) && 
                (
                    this.Currency == input.Currency ||
                    (this.Currency != null &&
                    this.Currency.Equals(input.Currency))
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
                if (this.DepositFee != null)
                    hashCode = hashCode * 59 + this.DepositFee.GetHashCode();
                if (this.WithdrawalFee != null)
                    hashCode = hashCode * 59 + this.WithdrawalFee.GetHashCode();
                if (this.DepositTax != null)
                    hashCode = hashCode * 59 + this.DepositTax.GetHashCode();
                if (this.WithdrawalTax != null)
                    hashCode = hashCode * 59 + this.WithdrawalTax.GetHashCode();
                if (this.Currency != null)
                    hashCode = hashCode * 59 + this.Currency.GetHashCode();
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
