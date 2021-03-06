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
    /// AkbankDirektCommissionOutputModel
    /// </summary>
    [DataContract]
        public partial class AkbankDirektCommissionOutputModel :  IEquatable<AkbankDirektCommissionOutputModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AkbankDirektCommissionOutputModel" /> class.
        /// </summary>
        /// <param name="depositFee">depositFee.</param>
        /// <param name="depositMaxFee">depositMaxFee.</param>
        /// <param name="depositTax">depositTax.</param>
        /// <param name="depositMinAmount">depositMinAmount.</param>
        public AkbankDirektCommissionOutputModel(double? depositFee = default(double?), int? depositMaxFee = default(int?), double? depositTax = default(double?), double? depositMinAmount = default(double?))
        {
            this.DepositFee = depositFee;
            this.DepositMaxFee = depositMaxFee;
            this.DepositTax = depositTax;
            this.DepositMinAmount = depositMinAmount;
        }
        
        /// <summary>
        /// Gets or Sets DepositFee
        /// </summary>
        [DataMember(Name="depositFee", EmitDefaultValue=false)]
        public double? DepositFee { get; set; }

        /// <summary>
        /// Gets or Sets DepositMaxFee
        /// </summary>
        [DataMember(Name="depositMaxFee", EmitDefaultValue=false)]
        public int? DepositMaxFee { get; set; }

        /// <summary>
        /// Gets or Sets DepositTax
        /// </summary>
        [DataMember(Name="depositTax", EmitDefaultValue=false)]
        public double? DepositTax { get; set; }

        /// <summary>
        /// Gets or Sets DepositMinAmount
        /// </summary>
        [DataMember(Name="depositMinAmount", EmitDefaultValue=false)]
        public double? DepositMinAmount { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AkbankDirektCommissionOutputModel {\n");
            sb.Append("  DepositFee: ").Append(DepositFee).Append("\n");
            sb.Append("  DepositMaxFee: ").Append(DepositMaxFee).Append("\n");
            sb.Append("  DepositTax: ").Append(DepositTax).Append("\n");
            sb.Append("  DepositMinAmount: ").Append(DepositMinAmount).Append("\n");
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
            return this.Equals(input as AkbankDirektCommissionOutputModel);
        }

        /// <summary>
        /// Returns true if AkbankDirektCommissionOutputModel instances are equal
        /// </summary>
        /// <param name="input">Instance of AkbankDirektCommissionOutputModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AkbankDirektCommissionOutputModel input)
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
                    this.DepositMaxFee == input.DepositMaxFee ||
                    (this.DepositMaxFee != null &&
                    this.DepositMaxFee.Equals(input.DepositMaxFee))
                ) && 
                (
                    this.DepositTax == input.DepositTax ||
                    (this.DepositTax != null &&
                    this.DepositTax.Equals(input.DepositTax))
                ) && 
                (
                    this.DepositMinAmount == input.DepositMinAmount ||
                    (this.DepositMinAmount != null &&
                    this.DepositMinAmount.Equals(input.DepositMinAmount))
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
                if (this.DepositMaxFee != null)
                    hashCode = hashCode * 59 + this.DepositMaxFee.GetHashCode();
                if (this.DepositTax != null)
                    hashCode = hashCode * 59 + this.DepositTax.GetHashCode();
                if (this.DepositMinAmount != null)
                    hashCode = hashCode * 59 + this.DepositMinAmount.GetHashCode();
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
