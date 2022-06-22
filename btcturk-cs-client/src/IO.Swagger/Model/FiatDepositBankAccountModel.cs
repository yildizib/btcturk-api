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
    /// FiatDepositBankAccountModel
    /// </summary>
    [DataContract]
        public partial class FiatDepositBankAccountModel :  IEquatable<FiatDepositBankAccountModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="FiatDepositBankAccountModel" /> class.
        /// </summary>
        /// <param name="slug">slug.</param>
        /// <param name="code">code.</param>
        /// <param name="name">name.</param>
        /// <param name="statusTransfer">statusTransfer.</param>
        /// <param name="statusAcceptEFT">statusAcceptEFT.</param>
        /// <param name="ban">ban.</param>
        /// <param name="owner">owner.</param>
        /// <param name="darkLogo">darkLogo.</param>
        /// <param name="lightLogo">lightLogo.</param>
        /// <param name="currencySymbol">currencySymbol.</param>
        public FiatDepositBankAccountModel(string slug = default(string), string code = default(string), string name = default(string), bool? statusTransfer = default(bool?), bool? statusAcceptEFT = default(bool?), string ban = default(string), string owner = default(string), string darkLogo = default(string), string lightLogo = default(string), string currencySymbol = default(string))
        {
            this.Slug = slug;
            this.Code = code;
            this.Name = name;
            this.StatusTransfer = statusTransfer;
            this.StatusAcceptEFT = statusAcceptEFT;
            this.Iban = ban;
            this.Owner = owner;
            this.DarkLogo = darkLogo;
            this.LightLogo = lightLogo;
            this.CurrencySymbol = currencySymbol;
        }
        
        /// <summary>
        /// Gets or Sets Slug
        /// </summary>
        [DataMember(Name="slug", EmitDefaultValue=false)]
        public string Slug { get; set; }

        /// <summary>
        /// Gets or Sets Code
        /// </summary>
        [DataMember(Name="code", EmitDefaultValue=false)]
        public string Code { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets StatusTransfer
        /// </summary>
        [DataMember(Name="statusTransfer", EmitDefaultValue=false)]
        public bool? StatusTransfer { get; set; }

        /// <summary>
        /// Gets or Sets StatusAcceptEFT
        /// </summary>
        [DataMember(Name="statusAcceptEFT", EmitDefaultValue=false)]
        public bool? StatusAcceptEFT { get; set; }

        /// <summary>
        /// Gets or Sets Iban
        /// </summary>
        [DataMember(Name="iban", EmitDefaultValue=false)]
        public string Iban { get; set; }

        /// <summary>
        /// Gets or Sets Owner
        /// </summary>
        [DataMember(Name="owner", EmitDefaultValue=false)]
        public string Owner { get; set; }

        /// <summary>
        /// Gets or Sets DarkLogo
        /// </summary>
        [DataMember(Name="darkLogo", EmitDefaultValue=false)]
        public string DarkLogo { get; set; }

        /// <summary>
        /// Gets or Sets LightLogo
        /// </summary>
        [DataMember(Name="lightLogo", EmitDefaultValue=false)]
        public string LightLogo { get; set; }

        /// <summary>
        /// Gets or Sets CurrencySymbol
        /// </summary>
        [DataMember(Name="currencySymbol", EmitDefaultValue=false)]
        public string CurrencySymbol { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class FiatDepositBankAccountModel {\n");
            sb.Append("  Slug: ").Append(Slug).Append("\n");
            sb.Append("  Code: ").Append(Code).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  StatusTransfer: ").Append(StatusTransfer).Append("\n");
            sb.Append("  StatusAcceptEFT: ").Append(StatusAcceptEFT).Append("\n");
            sb.Append("  Iban: ").Append(Iban).Append("\n");
            sb.Append("  Owner: ").Append(Owner).Append("\n");
            sb.Append("  DarkLogo: ").Append(DarkLogo).Append("\n");
            sb.Append("  LightLogo: ").Append(LightLogo).Append("\n");
            sb.Append("  CurrencySymbol: ").Append(CurrencySymbol).Append("\n");
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
            return this.Equals(input as FiatDepositBankAccountModel);
        }

        /// <summary>
        /// Returns true if FiatDepositBankAccountModel instances are equal
        /// </summary>
        /// <param name="input">Instance of FiatDepositBankAccountModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(FiatDepositBankAccountModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Slug == input.Slug ||
                    (this.Slug != null &&
                    this.Slug.Equals(input.Slug))
                ) && 
                (
                    this.Code == input.Code ||
                    (this.Code != null &&
                    this.Code.Equals(input.Code))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.StatusTransfer == input.StatusTransfer ||
                    (this.StatusTransfer != null &&
                    this.StatusTransfer.Equals(input.StatusTransfer))
                ) && 
                (
                    this.StatusAcceptEFT == input.StatusAcceptEFT ||
                    (this.StatusAcceptEFT != null &&
                    this.StatusAcceptEFT.Equals(input.StatusAcceptEFT))
                ) && 
                (
                    this.Iban == input.Iban ||
                    (this.Iban != null &&
                    this.Iban.Equals(input.Iban))
                ) && 
                (
                    this.Owner == input.Owner ||
                    (this.Owner != null &&
                    this.Owner.Equals(input.Owner))
                ) && 
                (
                    this.DarkLogo == input.DarkLogo ||
                    (this.DarkLogo != null &&
                    this.DarkLogo.Equals(input.DarkLogo))
                ) && 
                (
                    this.LightLogo == input.LightLogo ||
                    (this.LightLogo != null &&
                    this.LightLogo.Equals(input.LightLogo))
                ) && 
                (
                    this.CurrencySymbol == input.CurrencySymbol ||
                    (this.CurrencySymbol != null &&
                    this.CurrencySymbol.Equals(input.CurrencySymbol))
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
                if (this.Slug != null)
                    hashCode = hashCode * 59 + this.Slug.GetHashCode();
                if (this.Code != null)
                    hashCode = hashCode * 59 + this.Code.GetHashCode();
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.StatusTransfer != null)
                    hashCode = hashCode * 59 + this.StatusTransfer.GetHashCode();
                if (this.StatusAcceptEFT != null)
                    hashCode = hashCode * 59 + this.StatusAcceptEFT.GetHashCode();
                if (this.Iban != null)
                    hashCode = hashCode * 59 + this.Iban.GetHashCode();
                if (this.Owner != null)
                    hashCode = hashCode * 59 + this.Owner.GetHashCode();
                if (this.DarkLogo != null)
                    hashCode = hashCode * 59 + this.DarkLogo.GetHashCode();
                if (this.LightLogo != null)
                    hashCode = hashCode * 59 + this.LightLogo.GetHashCode();
                if (this.CurrencySymbol != null)
                    hashCode = hashCode * 59 + this.CurrencySymbol.GetHashCode();
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
