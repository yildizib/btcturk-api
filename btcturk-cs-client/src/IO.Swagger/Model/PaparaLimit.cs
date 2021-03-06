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
    /// PaparaLimit
    /// </summary>
    [DataContract]
        public partial class PaparaLimit :  IEquatable<PaparaLimit>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="PaparaLimit" /> class.
        /// </summary>
        /// <param name="maxDepositFeeAmount">maxDepositFeeAmount.</param>
        /// <param name="minDepositAmount">minDepositAmount.</param>
        /// <param name="maxDepositAmount">maxDepositAmount.</param>
        /// <param name="minWithdrawalAmounts">minWithdrawalAmounts.</param>
        /// <param name="maxWithdrawalFeeAmount">maxWithdrawalFeeAmount.</param>
        /// <param name="minWithdrawalPerTransaction">minWithdrawalPerTransaction.</param>
        public PaparaLimit(double? maxDepositFeeAmount = default(double?), double? minDepositAmount = default(double?), double? maxDepositAmount = default(double?), double? minWithdrawalAmounts = default(double?), double? maxWithdrawalFeeAmount = default(double?), double? minWithdrawalPerTransaction = default(double?))
        {
            this.MaxDepositFeeAmount = maxDepositFeeAmount;
            this.MinDepositAmount = minDepositAmount;
            this.MaxDepositAmount = maxDepositAmount;
            this.MinWithdrawalAmounts = minWithdrawalAmounts;
            this.MaxWithdrawalFeeAmount = maxWithdrawalFeeAmount;
            this.MinWithdrawalPerTransaction = minWithdrawalPerTransaction;
        }
        
        /// <summary>
        /// Gets or Sets MaxDepositFeeAmount
        /// </summary>
        [DataMember(Name="maxDepositFeeAmount", EmitDefaultValue=false)]
        public double? MaxDepositFeeAmount { get; set; }

        /// <summary>
        /// Gets or Sets MinDepositAmount
        /// </summary>
        [DataMember(Name="minDepositAmount", EmitDefaultValue=false)]
        public double? MinDepositAmount { get; set; }

        /// <summary>
        /// Gets or Sets MaxDepositAmount
        /// </summary>
        [DataMember(Name="maxDepositAmount", EmitDefaultValue=false)]
        public double? MaxDepositAmount { get; set; }

        /// <summary>
        /// Gets or Sets MinWithdrawalAmounts
        /// </summary>
        [DataMember(Name="minWithdrawalAmounts", EmitDefaultValue=false)]
        public double? MinWithdrawalAmounts { get; set; }

        /// <summary>
        /// Gets or Sets MaxWithdrawalFeeAmount
        /// </summary>
        [DataMember(Name="maxWithdrawalFeeAmount", EmitDefaultValue=false)]
        public double? MaxWithdrawalFeeAmount { get; set; }

        /// <summary>
        /// Gets or Sets MinWithdrawalPerTransaction
        /// </summary>
        [DataMember(Name="minWithdrawalPerTransaction", EmitDefaultValue=false)]
        public double? MinWithdrawalPerTransaction { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class PaparaLimit {\n");
            sb.Append("  MaxDepositFeeAmount: ").Append(MaxDepositFeeAmount).Append("\n");
            sb.Append("  MinDepositAmount: ").Append(MinDepositAmount).Append("\n");
            sb.Append("  MaxDepositAmount: ").Append(MaxDepositAmount).Append("\n");
            sb.Append("  MinWithdrawalAmounts: ").Append(MinWithdrawalAmounts).Append("\n");
            sb.Append("  MaxWithdrawalFeeAmount: ").Append(MaxWithdrawalFeeAmount).Append("\n");
            sb.Append("  MinWithdrawalPerTransaction: ").Append(MinWithdrawalPerTransaction).Append("\n");
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
            return this.Equals(input as PaparaLimit);
        }

        /// <summary>
        /// Returns true if PaparaLimit instances are equal
        /// </summary>
        /// <param name="input">Instance of PaparaLimit to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(PaparaLimit input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.MaxDepositFeeAmount == input.MaxDepositFeeAmount ||
                    (this.MaxDepositFeeAmount != null &&
                    this.MaxDepositFeeAmount.Equals(input.MaxDepositFeeAmount))
                ) && 
                (
                    this.MinDepositAmount == input.MinDepositAmount ||
                    (this.MinDepositAmount != null &&
                    this.MinDepositAmount.Equals(input.MinDepositAmount))
                ) && 
                (
                    this.MaxDepositAmount == input.MaxDepositAmount ||
                    (this.MaxDepositAmount != null &&
                    this.MaxDepositAmount.Equals(input.MaxDepositAmount))
                ) && 
                (
                    this.MinWithdrawalAmounts == input.MinWithdrawalAmounts ||
                    (this.MinWithdrawalAmounts != null &&
                    this.MinWithdrawalAmounts.Equals(input.MinWithdrawalAmounts))
                ) && 
                (
                    this.MaxWithdrawalFeeAmount == input.MaxWithdrawalFeeAmount ||
                    (this.MaxWithdrawalFeeAmount != null &&
                    this.MaxWithdrawalFeeAmount.Equals(input.MaxWithdrawalFeeAmount))
                ) && 
                (
                    this.MinWithdrawalPerTransaction == input.MinWithdrawalPerTransaction ||
                    (this.MinWithdrawalPerTransaction != null &&
                    this.MinWithdrawalPerTransaction.Equals(input.MinWithdrawalPerTransaction))
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
                if (this.MaxDepositFeeAmount != null)
                    hashCode = hashCode * 59 + this.MaxDepositFeeAmount.GetHashCode();
                if (this.MinDepositAmount != null)
                    hashCode = hashCode * 59 + this.MinDepositAmount.GetHashCode();
                if (this.MaxDepositAmount != null)
                    hashCode = hashCode * 59 + this.MaxDepositAmount.GetHashCode();
                if (this.MinWithdrawalAmounts != null)
                    hashCode = hashCode * 59 + this.MinWithdrawalAmounts.GetHashCode();
                if (this.MaxWithdrawalFeeAmount != null)
                    hashCode = hashCode * 59 + this.MaxWithdrawalFeeAmount.GetHashCode();
                if (this.MinWithdrawalPerTransaction != null)
                    hashCode = hashCode * 59 + this.MinWithdrawalPerTransaction.GetHashCode();
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
