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
    /// CommissionOutputModel
    /// </summary>
    [DataContract]
        public partial class CommissionOutputModel :  IEquatable<CommissionOutputModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CommissionOutputModel" /> class.
        /// </summary>
        /// <param name="paparaCommissions">paparaCommissions.</param>
        /// <param name="akbankDirektCommissions">akbankDirektCommissions.</param>
        /// <param name="bankCommissions">bankCommissions.</param>
        /// <param name="bankCommissionList">bankCommissionList.</param>
        /// <param name="cryptoCommissions">cryptoCommissions.</param>
        public CommissionOutputModel(PaparaCommissionOutputModel paparaCommissions = default(PaparaCommissionOutputModel), AkbankDirektCommissionOutputModel akbankDirektCommissions = default(AkbankDirektCommissionOutputModel), BankCommissionOutputModel bankCommissions = default(BankCommissionOutputModel), List<BankCommissionOutputModel> bankCommissionList = default(List<BankCommissionOutputModel>), List<CryptoCommissionOutputModel> cryptoCommissions = default(List<CryptoCommissionOutputModel>))
        {
            this.PaparaCommissions = paparaCommissions;
            this.AkbankDirektCommissions = akbankDirektCommissions;
            this.BankCommissions = bankCommissions;
            this.BankCommissionList = bankCommissionList;
            this.CryptoCommissions = cryptoCommissions;
        }
        
        /// <summary>
        /// Gets or Sets PaparaCommissions
        /// </summary>
        [DataMember(Name="paparaCommissions", EmitDefaultValue=false)]
        public PaparaCommissionOutputModel PaparaCommissions { get; set; }

        /// <summary>
        /// Gets or Sets AkbankDirektCommissions
        /// </summary>
        [DataMember(Name="akbankDirektCommissions", EmitDefaultValue=false)]
        public AkbankDirektCommissionOutputModel AkbankDirektCommissions { get; set; }

        /// <summary>
        /// Gets or Sets BankCommissions
        /// </summary>
        [DataMember(Name="bankCommissions", EmitDefaultValue=false)]
        public BankCommissionOutputModel BankCommissions { get; set; }

        /// <summary>
        /// Gets or Sets BankCommissionList
        /// </summary>
        [DataMember(Name="bankCommissionList", EmitDefaultValue=false)]
        public List<BankCommissionOutputModel> BankCommissionList { get; set; }

        /// <summary>
        /// Gets or Sets CryptoCommissions
        /// </summary>
        [DataMember(Name="cryptoCommissions", EmitDefaultValue=false)]
        public List<CryptoCommissionOutputModel> CryptoCommissions { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class CommissionOutputModel {\n");
            sb.Append("  PaparaCommissions: ").Append(PaparaCommissions).Append("\n");
            sb.Append("  AkbankDirektCommissions: ").Append(AkbankDirektCommissions).Append("\n");
            sb.Append("  BankCommissions: ").Append(BankCommissions).Append("\n");
            sb.Append("  BankCommissionList: ").Append(BankCommissionList).Append("\n");
            sb.Append("  CryptoCommissions: ").Append(CryptoCommissions).Append("\n");
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
            return this.Equals(input as CommissionOutputModel);
        }

        /// <summary>
        /// Returns true if CommissionOutputModel instances are equal
        /// </summary>
        /// <param name="input">Instance of CommissionOutputModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(CommissionOutputModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.PaparaCommissions == input.PaparaCommissions ||
                    (this.PaparaCommissions != null &&
                    this.PaparaCommissions.Equals(input.PaparaCommissions))
                ) && 
                (
                    this.AkbankDirektCommissions == input.AkbankDirektCommissions ||
                    (this.AkbankDirektCommissions != null &&
                    this.AkbankDirektCommissions.Equals(input.AkbankDirektCommissions))
                ) && 
                (
                    this.BankCommissions == input.BankCommissions ||
                    (this.BankCommissions != null &&
                    this.BankCommissions.Equals(input.BankCommissions))
                ) && 
                (
                    this.BankCommissionList == input.BankCommissionList ||
                    this.BankCommissionList != null &&
                    input.BankCommissionList != null &&
                    this.BankCommissionList.SequenceEqual(input.BankCommissionList)
                ) && 
                (
                    this.CryptoCommissions == input.CryptoCommissions ||
                    this.CryptoCommissions != null &&
                    input.CryptoCommissions != null &&
                    this.CryptoCommissions.SequenceEqual(input.CryptoCommissions)
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
                if (this.PaparaCommissions != null)
                    hashCode = hashCode * 59 + this.PaparaCommissions.GetHashCode();
                if (this.AkbankDirektCommissions != null)
                    hashCode = hashCode * 59 + this.AkbankDirektCommissions.GetHashCode();
                if (this.BankCommissions != null)
                    hashCode = hashCode * 59 + this.BankCommissions.GetHashCode();
                if (this.BankCommissionList != null)
                    hashCode = hashCode * 59 + this.BankCommissionList.GetHashCode();
                if (this.CryptoCommissions != null)
                    hashCode = hashCode * 59 + this.CryptoCommissions.GetHashCode();
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
